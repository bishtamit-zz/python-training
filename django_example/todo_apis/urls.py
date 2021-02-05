from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from todo_apis import views

app_name = 'todo_apis'

urlpatterns = [
    path('', views.tasks_apiview),
    path('<int:pk>', views.task_apiview)
]

urlpatterns = format_suffix_patterns(urlpatterns)

