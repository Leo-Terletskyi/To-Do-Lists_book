from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response

from .models import ToDoList, ToDoAction
from .serializers import ToDoListListSerializer, ToDoListCreateSerializer, ToDoListRetrieveSerializer, ToDoActionSerializer


class ToDoListListAPIView(generics.ListAPIView):
    serializer_class = ToDoListListSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        qs = ToDoList.objects.filter(user=user).select_related('user')
        return qs


class ToDoListCreateAPIView(generics.CreateAPIView):
    serializer_class = ToDoListCreateSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ToDoListRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = ToDoListRetrieveSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        try:
            return ToDoList.objects.get(user=self.request.user, slug=self.kwargs.get('slug'))
        except ToDoList.DoesNotExist or AttributeError:
            raise Http404


class ToDoActionCreateAPIView(generics.CreateAPIView):
    serializer_class = ToDoActionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        to_do_list = ToDoList.objects.get(slug=self.kwargs.get('slug'), user=self.request.user)
        serializer.save(to_do_list=to_do_list)


class ToDoActionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoActionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        try:
            return ToDoAction.objects.get(to_do_list__user=self.request.user, pk=self.kwargs.get('pk'))
        except ToDoAction.DoesNotExist or AttributeError:
            raise Http404


