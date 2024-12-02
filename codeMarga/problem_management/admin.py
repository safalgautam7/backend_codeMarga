from django.contrib import admin
from .models import Category, Problem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('difficulty', 'category')
