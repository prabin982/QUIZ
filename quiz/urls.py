from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.home, name='home'),
    path('quizzes/', views.quiz_list, name='quiz_list'),
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
    path('quiz/<int:quiz_id>/start/', views.start_quiz, name='start_quiz'),
    path('quiz/<int:quiz_id>/question/<int:question_num>/', views.quiz_question, name='quiz_question'),
    path('quiz/<int:quiz_id>/submit/', views.submit_quiz, name='submit_quiz'),
    path('quiz/<int:quiz_id>/results/<int:attempt_id>/', views.quiz_results, name='quiz_results'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('leaderboard/<int:quiz_id>/', views.quiz_leaderboard, name='quiz_leaderboard'),
    path('my-results/', views.my_results, name='my_results'),
]
