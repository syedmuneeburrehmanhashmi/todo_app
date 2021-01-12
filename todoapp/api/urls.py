from django.urls import path
from .views import api_overview, task_list, task_detail, task_create, task_delete, task_update

urlpatterns = [
    path('',api_overview, name = "api-overview"),
    path('task-create/', task_create, name = "task-create"),
    path('task-list/', task_list, name = "task-list"),
    path('task-detail/<str:pk>/', task_detail, name = "task-detail"),
    path('task-delete/<str:pk>/', task_delete, name = "task-delete"),
    path('task-update/<str:pk>/', task_update, name = "task-update")
]
