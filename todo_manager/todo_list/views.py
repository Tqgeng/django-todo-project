from django.http import (
    HttpRequest,
    HttpResponse,
)
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import TodoItem


def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = TodoItem.objects.all()
    return render(
        request,
        template_name="todo_list/index.html",
        context={"todo_items": todo_items},
    )


class TodoListIndexView(ListView):
    template_name = "todo_list/index.html"
    queryset = TodoItem.objects.all()[:3]


class TodoListView(ListView):
    model = TodoItem


class TodoListCompleteView(ListView):
    queryset = TodoItem.objects.filter(complete=True).all()


class TodoDetailView(DetailView):
    model = TodoItem
