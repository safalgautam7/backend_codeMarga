from rest_framework import serializers
from .models import Category, Problem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProblemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Problem
        fields = [
            'id', 'title', 'description', 'input_format', 
            'output_format', 'constraints', 'sample_input', 
            'sample_output', 'category', 'difficulty', 
            'created_at', 'updated_at',
        ]
