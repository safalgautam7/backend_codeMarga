from django.db import models

class Problem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    examples = models.JSONField(
        help_text=(
            "Provide examples in the format: "
            "[{'input': '...', 'output': '...', 'explanation': '...'}, ...]"
        )
    )
    class_name = models.CharField(max_length=50)
    method_name = models.CharField(max_length=50)
    
    default_code = models.JSONField(
        help_text=(
            "Provide the default code as a dictionary, e.g., "
            "{'python': '...', 'cpp': '...', 'java': '...'}."
        )
    )
    
    constraints = models.TextField(
        blank=True,
        help_text="Optional: Specify constraints like input size, time limits, etc."
    )
    
    followup = models.TextField(
        blank=True,
        help_text="Optional: Add follow-up questions or problem extensions."
    )

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100)
    problems = models.ManyToManyField(Problem, related_name='categories')

    def __str__(self):
        return self.name


class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input_data = models.JSONField(help_text="Provide arguments in json")
    expected_output = models.JSONField(help_text="Provide expected output in json")

    def __str__(self):
        return f"TestCase for {self.problem.title}"
