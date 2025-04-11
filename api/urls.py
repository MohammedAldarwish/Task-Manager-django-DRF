from django.urls import path, include
from rest_framework import routers
from .views import TaskViewsets


router = routers.DefaultRouter()
router.register('tasks', TaskViewsets, basename='tasks')


urlpatterns = [
    path('', include(router.urls))

]
