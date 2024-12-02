from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Problem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=50, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ])
    constraints = models.TextField()
    example_input = models.TextField(blank=True, null=True)  # Optional input example
    example_output = models.TextField(blank=True, null=True) # Optional output example
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="problems")

    def __str__(self):
        return self.title

