from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Avg, Count, Q
from datetime import timedelta
import json

from .models import Quiz, Question, Choice, QuizAttempt, UserAnswer, Category


def home(request):
    recent_quizzes = Quiz.objects.filter(is_active=True).order_by('-created_at')[:6]
    categories = Category.objects.all()
    
    context = {
        'recent_quizzes': recent_quizzes,
        'categories': categories,
    }
    return render(request, 'quiz/home.html', context)


def quiz_list(request):
    quizzes = Quiz.objects.filter(is_active=True).order_by('-created_at')
    categories = Category.objects.all()
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        quizzes = quizzes.filter(category_id=category_id)
    
    # Filter by difficulty
    difficulty = request.GET.get('difficulty')
    if difficulty:
        quizzes = quizzes.filter(difficulty=difficulty)
    
    context = {
        'quizzes': quizzes,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None,
        'selected_difficulty': difficulty,
    }
    return render(request, 'quiz/quiz_list.html', context)


def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
    user_attempts = []
    
    if request.user.is_authenticated:
        user_attempts = QuizAttempt.objects.filter(
            user=request.user, 
            quiz=quiz, 
            is_completed=True
        ).order_by('-completed_at')[:5]
    
    context = {
        'quiz': quiz,
        'user_attempts': user_attempts,
        'total_questions': quiz.questions.filter(is_active=True).count(),
    }
    return render(request, 'quiz/quiz_detail.html', context)


@login_required
def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
    
    # Create new quiz attempt
    attempt = QuizAttempt.objects.create(
        user=request.user,
        quiz=quiz,
        started_at=timezone.now(),
        total_questions=quiz.questions_count
    )
    
    # Store attempt ID in session
    request.session['quiz_attempt_id'] = attempt.id
    request.session['quiz_questions'] = [q.id for q in quiz.get_random_questions()]
    request.session['current_question'] = 0
    
    return redirect('quiz:quiz_question', quiz_id=quiz_id, question_num=1)


@login_required
def quiz_question(request, quiz_id, question_num):
    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
    attempt_id = request.session.get('quiz_attempt_id')
    question_ids = request.session.get('quiz_questions', [])
    
    if not attempt_id or not question_ids:
        messages.error(request, 'Quiz session expired. Please start again.')
        return redirect('quiz:quiz_detail', quiz_id=quiz_id)
    
    attempt = get_object_or_404(QuizAttempt, id=attempt_id, user=request.user)
    
    if question_num > len(question_ids):
        return redirect('quiz:submit_quiz', quiz_id=quiz_id)
    
    question_id = question_ids[question_num - 1]
    question = get_object_or_404(Question, id=question_id)
    
    # Check if user already answered this question
    existing_answer = UserAnswer.objects.filter(
        attempt=attempt, 
        question=question
    ).first()
    
    context = {
        'quiz': quiz,
        'question': question,
        'question_num': question_num,
        'total_questions': len(question_ids),
        'existing_answer': existing_answer,
        'time_limit': question.time_limit,
    }
    return render(request, 'quiz/quiz_question.html', context)


@login_required
def submit_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id, is_active=True)
    attempt_id = request.session.get('quiz_attempt_id')
    
    if not attempt_id:
        messages.error(request, 'Quiz session expired.')
        return redirect('quiz:quiz_detail', quiz_id=quiz_id)
    
    attempt = get_object_or_404(QuizAttempt, id=attempt_id, user=request.user)
    
    if request.method == 'POST':
        # Process answer submission
        question_id = request.POST.get('question_id')
        choice_id = request.POST.get('choice_id')
        time_taken = int(request.POST.get('time_taken', 0))
        
        if question_id and choice_id:
            question = get_object_or_404(Question, id=question_id)
            choice = get_object_or_404(Choice, id=choice_id)
            
            # Save or update user answer
            user_answer, created = UserAnswer.objects.get_or_create(
                attempt=attempt,
                question=question,
                defaults={
                    'selected_choice': choice,
                    'is_correct': choice.is_correct,
                    'time_taken': time_taken
                }
            )
            
            if not created:
                user_answer.selected_choice = choice
                user_answer.is_correct = choice.is_correct
                user_answer.time_taken = time_taken
                user_answer.save()
        
        # Check if this is the final submission
        if request.POST.get('final_submit'):
            # Calculate final score
            correct_answers = UserAnswer.objects.filter(
                attempt=attempt, 
                is_correct=True
            ).count()
            
            attempt.score = correct_answers
            attempt.is_completed = True
            attempt.time_taken = timezone.now() - attempt.started_at
            attempt.save()
            
            # Clear session
            request.session.pop('quiz_attempt_id', None)
            request.session.pop('quiz_questions', None)
            request.session.pop('current_question', None)
            
            return redirect('quiz:quiz_results', quiz_id=quiz_id, attempt_id=attempt.id)
        
        # Move to next question
        current_question = request.session.get('current_question', 0)
        next_question = current_question + 1
        request.session['current_question'] = next_question
        
        question_ids = request.session.get('quiz_questions', [])
        if next_question < len(question_ids):
            return redirect('quiz:quiz_question', quiz_id=quiz_id, question_num=next_question + 1)
        else:
            # Show final submission page
            context = {
                'quiz': quiz,
                'attempt': attempt,
                'total_questions': len(question_ids),
                'answered_questions': UserAnswer.objects.filter(attempt=attempt).count(),
            }
            return render(request, 'quiz/submit_quiz.html', context)
    
    # GET request - show submission page
    question_ids = request.session.get('quiz_questions', [])
    context = {
        'quiz': quiz,
        'attempt': attempt,
        'total_questions': len(question_ids),
        'answered_questions': UserAnswer.objects.filter(attempt=attempt).count(),
    }
    return render(request, 'quiz/submit_quiz.html', context)


@login_required
def quiz_results(request, quiz_id, attempt_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    attempt = get_object_or_404(QuizAttempt, id=attempt_id, user=request.user, quiz=quiz)
    
    user_answers = UserAnswer.objects.filter(attempt=attempt).select_related(
        'question', 'selected_choice'
    )
    
    context = {
        'quiz': quiz,
        'attempt': attempt,
        'user_answers': user_answers,
        'percentage': attempt.get_percentage(),
    }
    return render(request, 'quiz/quiz_results.html', context)


def leaderboard(request):
    # Overall leaderboard
    top_users = QuizAttempt.objects.filter(is_completed=True).values(
        'user__username'
    ).annotate(
        total_score=models.Sum('score'),
        total_attempts=Count('id'),
        avg_score=Avg('score')
    ).order_by('-total_score')[:10]
    
    recent_attempts = QuizAttempt.objects.filter(
        is_completed=True
    ).select_related('user', 'quiz').order_by('-completed_at')[:10]
    
    context = {
        'top_users': top_users,
        'recent_attempts': recent_attempts,
    }
    return render(request, 'quiz/leaderboard.html', context)


def quiz_leaderboard(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    
    top_attempts = QuizAttempt.objects.filter(
        quiz=quiz, 
        is_completed=True
    ).select_related('user').order_by('-score', 'time_taken')[:10]
    
    context = {
        'quiz': quiz,
        'top_attempts': top_attempts,
    }
    return render(request, 'quiz/quiz_leaderboard.html', context)


@login_required
def my_results(request):
    attempts = QuizAttempt.objects.filter(
        user=request.user, 
        is_completed=True
    ).select_related('quiz').order_by('-completed_at')
    
    context = {
        'attempts': attempts,
    }
    return render(request, 'quiz/my_results.html', context)
