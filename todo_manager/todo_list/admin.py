from django.contrib import admin

from todo_list.models import TodoItem


@admin.register(TodoItem)
class TodoItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "complete",
    )
    list_display_links = (
        "id",
        "title",
    )
