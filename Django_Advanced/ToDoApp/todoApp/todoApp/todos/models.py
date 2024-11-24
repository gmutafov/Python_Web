from django.contrib.auth import get_user_model
from django.db import models

from todoApp.todos.choices import StateChoices


# Create your models here.

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=15)


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    state = models.BooleanField(
        choices=[
            (True, StateChoices.DONE),
            (False, StateChoices.NOT_DONE),
        ],
        default=False,
    )

    assignees = models.ManyToManyField(UserModel, related_name="assigned_to", blank=True)

    def __str__(self):
        return self.title