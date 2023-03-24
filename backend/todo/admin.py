from django.contrib import admin

from .models import ToDoList, ToDoAction


@admin.register(ToDoAction)
class ToDoActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'to_do_list', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    exclude = ('slug',)
    search_fields = ('title',)
    list_filter = ('to_do_list',)
    list_per_page = 10


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at', 'updated_at')
    list_display_links = ('id', 'title')
    exclude = ('user', 'slug')
    search_fields = ('title',)
    list_filter = ('user',)
    list_per_page = 10

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)
