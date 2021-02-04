from django.urls import path
from todo import views
app_name = 'todo'

urlpatterns = [
    path('', views.list_view, name='index'),
    path('new', views.add, name='add'),
    path('<int:pk>', views.detail_view, name='detail'),
    path('<int:pk>/edit', views.edit, name='edit'),
    path('<int:pk>/delete', views.delete, name='delete')
]
