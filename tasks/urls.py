from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>', views.task, name='task'),
    path('new', views.new, name='new'),
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('edit/<int:task_id>', views.edit, name='edit')
]