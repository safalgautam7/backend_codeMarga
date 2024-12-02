import os
import django
import sys

# Add the backend directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Set the environment variable to point to your Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'codeMarga.settings')

# Initialize Django
django.setup()

from problem_management.models import Problem, Category
import json

def populate_problems():
    # File path to the JSON file
    file_path = os.path.join(os.path.dirname(__file__), '../data/problems.json')

    # Load the JSON data
    with open(file_path, 'r') as file:
        problems = json.load(file)

    for problem_data in problems:
        # Get or create the category
        category_name = problem_data['category']
        category, _ = Category.objects.get_or_create(name=category_name)

        Problem.objects.create(
            title=problem_data['title'],
            description=problem_data['description'],
            difficulty=problem_data['difficulty'],
            constraints=problem_data['constraints'],
            example_input=problem_data['example_input'],
            example_output=problem_data['example_output'],
            category=category
        ),

    print("Problems populated successfully!")

if __name__ == "__main__":
    populate_problems()
