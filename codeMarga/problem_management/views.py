from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Problem
from .serializers import CategorySerializer, ProblemSerializer

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class ProblemListView(APIView):
    def get(self, request):
        problems = Problem.objects.all()
        serializer = ProblemSerializer(problems, many=True)
        return Response(serializer.data)

class ProblemDetailView(APIView):
    def get(self, request, pk):
        try:
            problem = Problem.objects.get(pk=pk)
        except Problem.DoesNotExist:
            return Response({"error": "Problem not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProblemSerializer(problem)
        return Response(serializer.data)
