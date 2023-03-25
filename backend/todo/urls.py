from django.urls import path

from . import views


urlpatterns = [
    path('to-do-lists/', views.ToDoListListAPIView.as_view()),
    path('to-do-lists/<slug:slug>/', views.ToDoListRetrieveDestroyAPIView.as_view()),
    path('to-do-actions/<int:pk>/', views.ToDoActionRetrieveUpdateDestroyAPIView.as_view()),

]
