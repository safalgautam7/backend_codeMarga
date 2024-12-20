from django.contrib import admin
from .models import Problem, Category, TestCase, Example

class ExampleInline(admin.TabularInline):
    model = Example
    extra = 1  # Number of empty forms to show for adding examples


class TestCaseInline(admin.TabularInline):
    model = TestCase
    extra = 1  # Number of empty forms to show for adding test cases


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'class_name', 'method_name', 'created_at', 'updated_at')
    search_fields = ('title', 'class_name', 'method_name')
    list_filter = ('categories', 'created_at', 'updated_at')
    inlines = [ExampleInline, TestCaseInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('problem', 'input_data', 'expected_output')
    search_fields = ('problem__title',)
    list_filter = ('problem',)


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    list_display = ('problem', 'input_data', 'output_data', 'explanation')
    search_fields = ('problem__title',)
    list_filter = ('problem',)
