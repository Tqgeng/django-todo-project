from django import forms

from todo_list.models import TodoItem


class ToDoItemForm(forms.ModelForm):

    class Meta:
        model = TodoItem
        fields = ("title", "description")

        widgets = {
            "description": forms.Textarea(attrs={"cols": 20, "rows": 5}),
        }
