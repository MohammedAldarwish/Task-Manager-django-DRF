from django.db import models
from accounts.models import CustomUser

class TaskModel(models.Model):
    title = models.CharField(max_length=160)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(CustomUser, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

