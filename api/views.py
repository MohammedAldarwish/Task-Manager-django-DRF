from django.shortcuts import render
from rest_framework import viewsets
from .models import TaskModel
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

class TaskViewsets(viewsets.ModelViewSet):
    def get_queryset(self):
        return TaskModel.objects.filter(created_by=self.request.user).order_by('-created_at')

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)