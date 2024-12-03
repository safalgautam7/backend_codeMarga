from django.contrib import admin
from .models import Problem, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display only the 'name' field

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_categories')  # Removed 'difficulty'
    
    # Custom method to display categories related to a problem
    def get_categories(self, obj):
        # Access the reverse relation using 'categories' as defined in related_name
        return ", ".join([category.name for category in obj.categories.all()])
    
    get_categories.short_description = 'Categories'  # Display name in the admin panel

admin.site.register(Category, CategoryAdmin)
admin.site.register(Problem, ProblemAdmin)
