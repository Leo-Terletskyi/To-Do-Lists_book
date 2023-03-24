from django.contrib import admin

from .models import ToDoList, ToDoAction


admin.site.register(ToDoList)
admin.site.register(ToDoAction)

