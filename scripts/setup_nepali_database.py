#!/usr/bin/env python
"""
Database setup script for Nepali Quiz Platform
Created by Prabin Dhungana
Run this script to create Nepal-specific sample data
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_platform.settings')
django.setup()

from django.contrib.auth.models import User
from quiz.models import Category, Quiz, Question, Choice

def create_nepali_sample_data():
    print("Creating Nepali sample data for Quiz Platform...")
    print("Created by: Prabin Dhungana")
    print("=" * 50)
    
    # Create admin user with username 'pad'
    if not User.objects.filter(username='pad').exists():
        admin_user = User.objects.create_superuser(
            username='pad',
            email='prabin.dhungana@example.com',
            password='pad123',
            first_name='Prabin',
            last_name='Dhungana'
        )
        print("✓ Created admin user (username: pad, password: pad123)")
        print("  Created by: Prabin Dhungana")
    else:
        admin_user = User.objects.get(username='pad')
    
    # Create Nepal-specific categories
    categories_data = [
        {
            'name': 'Nepali General Knowledge', 
            'description': 'Test your knowledge about Nepal - culture, geography, and current affairs'
        },
        {
            'name': 'Science', 
            'description': 'Science and technology questions with focus on Nepal'
        },
        {
            'name': 'Nepali History', 
            'description': 'History of Nepal - ancient to modern times'
        },
        {
            'name': 'Sports', 
            'description': 'Sports in Nepal and international sports knowledge'
        },
    ]
    
    created_categories = {}
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        created_categories[cat_data['name']] = category
        if created:
            print(f"✓ Created category: {category.name}")
    
    # Create Nepali General Knowledge Quiz
    gk_quiz, created = Quiz.objects.get_or_create(
        title='Nepal General Knowledge Quiz',
        defaults={
            'description': 'Test your knowledge about beautiful Nepal - its culture, geography, and traditions. Created by Prabin Dhungana.',
            'category': created_categories['Nepali General Knowledge'],
            'difficulty': 'medium',
            'time_limit': 20,
            'questions_count': 8,
            'created_by': admin_user
        }
    )
    
    if created:
        print(f"✓ Created quiz: {gk_quiz.title}")
        
        gk_questions = [
            {
                'question_text': 'What is the capital city of Nepal?',
                'choices': [
                    {'text': 'Kathmandu', 'correct': True},
                    {'text': 'Pokhara', 'correct': False},
                    {'text': 'Lalitpur', 'correct': False},
                    {'text': 'Bhaktapur', 'correct': False},
                ]
            },
            {
                'question_text': 'Which mountain peak is the highest in the world and located in Nepal?',
                'choices': [
                    {'text': 'K2', 'correct': False},
                    {'text': 'Mount Everest (Sagarmatha)', 'correct': True},
                    {'text': 'Annapurna', 'correct': False},
                    {'text': 'Manaslu', 'correct': False},
                ]
            },
            {
                'question_text': 'What is the national flower of Nepal?',
                'choices': [
                    {'text': 'Rose', 'correct': False},
                    {'text': 'Lotus', 'correct': False},
                    {'text': 'Rhododendron (Lali Gurans)', 'correct': True},
                    {'text': 'Sunflower', 'correct': False},
                ]
            },
            {
                'question_text': 'Which river is considered the holiest river in Nepal?',
                'choices': [
                    {'text': 'Koshi River', 'correct': False},
                    {'text': 'Gandaki River', 'correct': False},
                    {'text': 'Bagmati River', 'correct': True},
                    {'text': 'Karnali River', 'correct': False},
                ]
            },
            {
                'question_text': 'What is the traditional greeting in Nepal?',
                'choices': [
                    {'text': 'Hello', 'correct': False},
                    {'text': 'Namaste', 'correct': True},
                    {'text': 'Sat Sri Akal', 'correct': False},
                    {'text': 'Adaab', 'correct': False},
                ]
            },
            {
                'question_text': 'Which festival is known as the festival of lights in Nepal?',
                'choices': [
                    {'text': 'Dashain', 'correct': False},
                    {'text': 'Tihar (Deepawali)', 'correct': True},
                    {'text': 'Holi', 'correct': False},
                    {'text': 'Teej', 'correct': False},
                ]
            },
            {
                'question_text': 'What is the currency of Nepal?',
                'choices': [
                    {'text': 'Rupee', 'correct': False},
                    {'text': 'Nepali Rupee', 'correct': True},
                    {'text': 'Taka', 'correct': False},
                    {'text': 'Dollar', 'correct': False},
                ]
            },
            {
                'question_text': 'Which UNESCO World Heritage Site is located in Kathmandu?',
                'choices': [
                    {'text': 'Taj Mahal', 'correct': False},
                    {'text': 'Pashupatinath Temple', 'correct': True},
                    {'text': 'Red Fort', 'correct': False},
                    {'text': 'Gateway of India', 'correct': False},
                ]
            },
        ]
        
        for q_data in gk_questions:
            question = Question.objects.create(
                quiz=gk_quiz,
                question_text=q_data['question_text'],
                question_type='multiple_choice',
                points=1,
                time_limit=90
            )
            
            for choice_data in q_data['choices']:
                Choice.objects.create(
                    question=question,
                    choice_text=choice_data['text'],
                    is_correct=choice_data['correct']
                )
            
            print(f"✓ Created question: {question.question_text[:40]}...")
    
    # Create Nepali History Quiz
    history_quiz, created = Quiz.objects.get_or_create(
        title='Nepal History Quiz',
        defaults={
            'description': 'Explore the rich history of Nepal from ancient times to modern era. Created by Prabin Dhungana.',
            'category': created_categories['Nepali History'],
            'difficulty': 'medium',
            'time_limit': 25,
            'questions_count': 6,
            'created_by': admin_user
        }
    )
    
    if created:
        print(f"✓ Created quiz: {history_quiz.title}")
        
        history_questions = [
            {
                'question_text': 'Who was the founder of modern Nepal?',
                'choices': [
                    {'text': 'King Tribhuvan', 'correct': False},
                    {'text': 'Prithvi Narayan Shah', 'correct': True},
                    {'text': 'King Mahendra', 'correct': False},
                    {'text': 'Jung Bahadur Rana', 'correct': False},
                ]
            },
            {
                'question_text': 'In which year did Nepal become a federal republic?',
                'choices': [
                    {'text': '2006', 'correct': False},
                    {'text': '2007', 'correct': False},
                    {'text': '2008', 'correct': True},
                    {'text': '2009', 'correct': False},
                ]
            },
            {
                'question_text': 'Which dynasty ruled Nepal for the longest period?',
                'choices': [
                    {'text': 'Malla Dynasty', 'correct': False},
                    {'text': 'Shah Dynasty', 'correct': True},
                    {'text': 'Licchavi Dynasty', 'correct': False},
                    {'text': 'Rana Dynasty', 'correct': False},
                ]
            },
            {
                'question_text': 'Who was the first Prime Minister of Nepal?',
                'choices': [
                    {'text': 'B.P. Koirala', 'correct': True},
                    {'text': 'Girija Prasad Koirala', 'correct': False},
                    {'text': 'Man Mohan Adhikari', 'correct': False},
                    {'text': 'Sher Bahadur Deuba', 'correct': False},
                ]
            },
            {
                'question_text': 'Which treaty established the modern boundary between Nepal and British India?',
                'choices': [
                    {'text': 'Treaty of Thapathali', 'correct': False},
                    {'text': 'Treaty of Sugauli', 'correct': True},
                    {'text': 'Treaty of Betrawati', 'correct': False},
                    {'text': 'Treaty of Kathmandu', 'correct': False},
                ]
            },
            {
                'question_text': 'When did the Gorkha earthquake occur that devastated Nepal?',
                'choices': [
                    {'text': '2014', 'correct': False},
                    {'text': '2015', 'correct': True},
                    {'text': '2016', 'correct': False},
                    {'text': '2017', 'correct': False},
                ]
            },
        ]
        
        for q_data in history_questions:
            question = Question.objects.create(
                quiz=history_quiz,
                question_text=q_data['question_text'],
                question_type='multiple_choice',
                points=1,
                time_limit=120
            )
            
            for choice_data in q_data['choices']:
                Choice.objects.create(
                    question=question,
                    choice_text=choice_data['text'],
                    is_correct=choice_data['correct']
                )
            
            print(f"✓ Created question: {question.question_text[:40]}...")
    
    # Create Sports Quiz
    sports_quiz, created = Quiz.objects.get_or_create(
        title='Nepal Sports Quiz',
        defaults={
            'description': 'Test your knowledge about sports in Nepal and international sports. Created by Prabin Dhungana.',
            'category': created_categories['Sports'],
            'difficulty': 'easy',
            'time_limit': 15,
            'questions_count': 5,
            'created_by': admin_user
        }
    )
    
    if created:
        print(f"✓ Created quiz: {sports_quiz.title}")
        
        sports_questions = [
            {
                'question_text': 'What is the most popular sport in Nepal?',
                'choices': [
                    {'text': 'Cricket', 'correct': False},
                    {'text': 'Football (Soccer)', 'correct': True},
                    {'text': 'Basketball', 'correct': False},
                    {'text': 'Volleyball', 'correct': False},
                ]
            },
            {
                'question_text': 'Which Nepali cricketer is known as the captain of Nepal national cricket team?',
                'choices': [
                    {'text': 'Paras Khadka', 'correct': True},
                    {'text': 'Sandeep Lamichhane', 'correct': False},
                    {'text': 'Gyanendra Malla', 'correct': False},
                    {'text': 'Dipendra Singh Airee', 'correct': False},
                ]
            },
            {
                'question_text': 'In which sport did Nepal first participate in the Olympics?',
                'choices': [
                    {'text': 'Swimming', 'correct': False},
                    {'text': 'Athletics', 'correct': True},
                    {'text': 'Boxing', 'correct': False},
                    {'text': 'Wrestling', 'correct': False},
                ]
            },
            {
                'question_text': 'What is the traditional sport of Nepal involving martial arts?',
                'choices': [
                    {'text': 'Karate', 'correct': False},
                    {'text': 'Taekwondo', 'correct': False},
                    {'text': 'Dandi Biyo', 'correct': False},
                    {'text': 'Khukuri Dance (Traditional)', 'correct': True},
                ]
            },
            {
                'question_text': 'Which stadium is the main football stadium in Kathmandu?',
                'choices': [
                    {'text': 'Wembley Stadium', 'correct': False},
                    {'text': 'Dasharath Stadium', 'correct': True},
                    {'text': 'Eden Gardens', 'correct': False},
                    {'text': 'Lord\'s Cricket Ground', 'correct': False},
                ]
            },
        ]
        
        for q_data in sports_questions:
            question = Question.objects.create(
                quiz=sports_quiz,
                question_text=q_data['question_text'],
                question_type='multiple_choice',
                points=1,
                time_limit=60
            )
            
            for choice_data in q_data['choices']:
                Choice.objects.create(
                    question=question,
                    choice_text=choice_data['text'],
                    is_correct=choice_data['correct']
                )
            
            print(f"✓ Created question: {question.question_text[:40]}...")
    
    # Create Science Quiz
    science_quiz, created = Quiz.objects.get_or_create(
        title='Science Knowledge Quiz',
        defaults={
            'description': 'Test your scientific knowledge with questions about physics, chemistry, biology, and technology. Created by Prabin Dhungana.',
            'category': created_categories['Science'],
            'difficulty': 'medium',
            'time_limit': 18,
            'questions_count': 6,
            'created_by': admin_user
        }
    )
    
    if created:
        print(f"✓ Created quiz: {science_quiz.title}")
        
        science_questions = [
            {
                'question_text': 'What is the chemical formula for water?',
                'choices': [
                    {'text': 'H2O', 'correct': True},
                    {'text': 'CO2', 'correct': False},
                    {'text': 'NaCl', 'correct': False},
                    {'text': 'CH4', 'correct': False},
                ]
            },
            {
                'question_text': 'Which planet is known as the Red Planet?',
                'choices': [
                    {'text': 'Venus', 'correct': False},
                    {'text': 'Mars', 'correct': True},
                    {'text': 'Jupiter', 'correct': False},
                    {'text': 'Saturn', 'correct': False},
                ]
            },
            {
                'question_text': 'What is the powerhouse of the cell?',
                'choices': [
                    {'text': 'Nucleus', 'correct': False},
                    {'text': 'Ribosome', 'correct': False},
                    {'text': 'Mitochondria', 'correct': True},
                    {'text': 'Chloroplast', 'correct': False},
                ]
            },
            {
                'question_text': 'Which gas is most abundant in Earth\'s atmosphere?',
                'choices': [
                    {'text': 'Oxygen', 'correct': False},
                    {'text': 'Carbon Dioxide', 'correct': False},
                    {'text': 'Nitrogen', 'correct': True},
                    {'text': 'Hydrogen', 'correct': False},
                ]
            },
            {
                'question_text': 'What is the speed of light in vacuum?',
                'choices': [
                    {'text': '300,000 km/s', 'correct': False},
                    {'text': '299,792,458 m/s', 'correct': True},
                    {'text': '150,000 km/s', 'correct': False},
                    {'text': '500,000 km/s', 'correct': False},
                ]
            },
            {
                'question_text': 'Which scientist developed the theory of evolution?',
                'choices': [
                    {'text': 'Albert Einstein', 'correct': False},
                    {'text': 'Isaac Newton', 'correct': False},
                    {'text': 'Charles Darwin', 'correct': True},
                    {'text': 'Galileo Galilei', 'correct': False},
                ]
            },
        ]
        
        for q_data in science_questions:
            question = Question.objects.create(
                quiz=science_quiz,
                question_text=q_data['question_text'],
                question_type='multiple_choice',
                points=1,
                time_limit=75
            )
            
            for choice_data in q_data['choices']:
                Choice.objects.create(
                    question=question,
                    choice_text=choice_data['text'],
                    is_correct=choice_data['correct']
                )
            
            print(f"✓ Created question: {question.question_text[:40]}...")
    
    print("\n🎉 Nepali Quiz Platform setup completed!")
    print("Created by: Prabin Dhungana")
    print("=" * 50)
    print("\nYou can now:")
    print("1. Run the server: python manage.py runserver")
    print("2. Access admin panel: http://127.0.0.1:8000/admin/")
    print("3. Login with: pad / pad123")
    print("4. Take Nepal-focused quizzes at: http://127.0.0.1:8000/")
    print("\nQuizzes created:")
    print("• Nepal General Knowledge Quiz (8 questions)")
    print("• Nepal History Quiz (6 questions)")
    print("• Nepal Sports Quiz (5 questions)")
    print("• Science Knowledge Quiz (6 questions)")
    print("\nAll content created by: Prabin Dhungana")

if __name__ == '__main__':
    create_nepali_sample_data()
