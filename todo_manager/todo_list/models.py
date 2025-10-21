from django.db import models


class TodoItem(models.Model):

    class Meta:
        ordering = ("id",)
        verbose_name = "ToDo Item"

    title = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
