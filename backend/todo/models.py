from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

user = get_user_model()


class ToDoList(models.Model):
    title = models.CharField(max_length=192)
    slug = models.SlugField(null=True, blank=True)
    user = models.ForeignKey(user, db_index=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'created by {self.user} - {self.title.upper()}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(force_insert=False, force_update=False, using=None, update_fields=None)

    class Meta:
        verbose_name = 'To-Do List'
        verbose_name_plural = 'To-Do Lists'
        ordering = ('-updated_at', 'created_at')
        constraints = [
            models.UniqueConstraint(fields=['user', 'title'], name='unique title for each user')
        ]


class ToDoAction(models.Model):
    title = models.CharField(max_length=192)
    completed = models.BooleanField(default=False)
    to_do_list = models.ForeignKey(ToDoList, db_index=True, related_name='actions', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.to_do_list}, to-do action named "{self.title}"'

    class Meta:
        verbose_name = 'To-Do Action'
        verbose_name_plural = 'To-Do Actions'
        ordering = ('-updated_at', '-created_at')
        constraints = [
            models.UniqueConstraint(fields=['to_do_list', 'title'], name='unique title for each to-do list')
        ]


