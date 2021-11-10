from django.urls import path
from . import views

urlpatterns = [
    # todo/
    path('', views.todo, name='todo'),
    # todo/<int:task_id>
    path('<int:task_id>', views.task, name='task'),
    # todo/notes
    path('notes/', views.note, name='note')
]