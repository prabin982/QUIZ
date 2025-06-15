#!/usr/bin/env python
"""
Database setup script for Quiz Platform
Run this script to create sample data for testing
"""

import os
import sys
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_platform.settings')
django.setup()

from django.contrib.auth.models import User
from quiz.models import Category, Quiz, Question, Choice

def create_sample_data():
    print("Creating sample data for Quiz Platform...")
    
    # Create superuser if it doesn't exist
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        print("✓ Created admin user (username: admin, password: admin123)")
    
    # Create categories
    categories_data = [
        {'name': 'General Knowledge', 'description': 'Test your general knowledge'},
        {'name': 'Science', 'description': 'Science and technology questions'},
        {'name': 'History', 'description': 'Historical events and figures'},
        {'name': 'Sports', 'description': 'Sports and games trivia'},
        {'name': 'Geography', 'description': 'World geography and locations'},
    ]
    
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data['name'],
            defaults={'description': cat_data['description']}
        )
        if created:
            print(f"✓ Created category: {category.name}")
    
    # Create sample quiz
    admin_user = User.objects.get(username='admin')
    science_category = Category.objects.get(name='Science')
    
    quiz, created = Quiz.objects.get_or_create(
        title='Basic Science Quiz',
        defaults={
            'description': 'Test your basic science knowledge with this fun quiz!',
            'category': science_category,
            'difficulty': 'easy',
            'time_limit': 15,
            'questions_count': 5,
            'created_by': admin_user
        }
    )
    
    if created:
        print(f"✓ Created quiz: {quiz.title}")
        
        # Create sample questions
        questions_data = [
            {
                'question_text': 'What is the chemical symbol for water?',
                'choices': [
                    {'text': 'H2O', 'correct': True},
                    {'text': 'CO2', 'correct': False},
                    {'text': 'NaCl', 'correct': False},
                    {'text': 'O2', 'correct': False},
                ]
            },
            {
                'question_text': 'How many planets are in our solar system?',
                'choices': [
                    {'text': '7', 'correct': False},
                    {'text': '8', 'correct': True},
                    {'text': '9', 'correct': False},
                    {'text': '10', 'correct': False},
                ]
            },
            {
                'question_text': 'What gas do plants absorb from the atmosphere during photosynthesis?',
                'choices': [
                    {'text': 'Oxygen', 'correct': False},
                    {'text': 'Nitrogen', 'correct': False},
                    {'text': 'Carbon Dioxide', 'correct': True},
                    {'text': 'Hydrogen', 'correct': False},
                ]
            },
            {
                'question_text': 'What is the hardest natural substance on Earth?',
                'choices': [
                    {'text': 'Gold', 'correct': False},
                    {'text': 'Iron', 'correct': False},
                    {'text': 'Diamond', 'correct': True},
                    {'text': 'Silver', 'correct': False},
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
        ]
        
        for q_data in questions_data:
            question = Question.objects.create(
                quiz=quiz,
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
            
            print(f"✓ Created question: {question.question_text[:50]}...")
    
    print("\n🎉 Sample data creation completed!")
    print("\nYou can now:")
    print("1. Run the server: python manage.py runserver")
    print("2. Access admin panel: http://127.0.0.1:8000/admin/")
    print("3. Login with: admin / admin123")
    print("4. Take the sample quiz at: http://127.0.0.1:8000/")

if __name__ == '__main__':
    create_sample_data()
