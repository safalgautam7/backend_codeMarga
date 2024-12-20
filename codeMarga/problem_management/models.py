from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="problems_in_category",
        help_text="Select a category for this problem."
    )

    def __str__(self):
        return self.title


class TestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input_data = models.JSONField(help_text="Provide arguments in json")
    expected_output = models.JSONField(help_text="Provide expected output in json")
