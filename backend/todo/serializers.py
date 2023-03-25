from rest_framework import serializers

from .models import ToDoList, ToDoAction


class ToDoActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoAction
        fields = ('id', 'title', 'completed')


class ToDoListListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDoList
        fields = ('id', 'title', 'slug')


class ToDoListRetrieveSerializer(serializers.ModelSerializer):
    actions = ToDoActionSerializer(many=True)

    class Meta:
        model = ToDoList
        fields = ('id', 'title', 'slug', 'actions')


