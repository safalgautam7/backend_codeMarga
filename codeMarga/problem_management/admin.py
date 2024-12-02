from django.contrib import admin
from .models import Problem, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Only display the 'name' field for the category

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'category',)  # Ensure 'created_at' is not here if it doesn't exist

admin.site.register(Category, CategoryAdmin)
admin.site.register(Problem, ProblemAdmin)
