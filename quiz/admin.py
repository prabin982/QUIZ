from django.contrib import admin
from .models import Category, Quiz, Question, Choice, QuizAttempt, UserAnswer


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'difficulty', 'questions_count', 'time_limit', 'is_active', 'created_at']
    list_filter = ['category', 'difficulty', 'is_active', 'created_at']
    search_fields = ['title', 'description']
    inlines = [QuestionInline]

    def save_model(self, request, obj, form, change):
        if not change:  # If creating new quiz
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'quiz', 'question_type', 'points', 'time_limit', 'is_active']
    list_filter = ['quiz', 'question_type', 'is_active']
    search_fields = ['question_text']
    inlines = [ChoiceInline]


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'score', 'total_questions', 'get_percentage', 'completed_at']
    list_filter = ['quiz', 'completed_at', 'is_completed']
    search_fields = ['user__username', 'quiz__title']
    readonly_fields = ['score', 'total_questions', 'time_taken', 'started_at', 'completed_at']

    def get_percentage(self, obj):
        return f"{obj.get_percentage()}%"
    get_percentage.short_description = 'Percentage'


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ['attempt', 'question', 'selected_choice', 'is_correct', 'time_taken']
    list_filter = ['is_correct', 'attempt__quiz']
    search_fields = ['attempt__user__username', 'question__question_text']
