from django.urls import path
from .views import CategoryListView, ProblemListView, ProblemDetailView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('problems/', ProblemListView.as_view(), name='problem-list'),
    path('problems/<int:pk>/', ProblemDetailView.as_view(), name='problem-detail'),
]
