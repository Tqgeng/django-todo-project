from django.urls import path

from . import views

app_name = "todo_list"
urlpatterns = [
    path("", views.TodoListIndexView.as_view(), name="index"),
    path("<int:pk>/", views.TodoDetailView.as_view(), name="detail"),
    path("list/", views.TodoListView.as_view(), name="list"),
    path("complete/", views.TodoListCompleteView.as_view(), name="complete"),
    path("create/", views.TodoItemCreateView.as_view(), name="create"),
]
