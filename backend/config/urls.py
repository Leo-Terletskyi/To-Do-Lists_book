from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView


urlpatterns = [
    # site urls
    path('', TemplateView.as_view(template_name='index.html')),
    path('sign-up/', TemplateView.as_view(template_name='index.html')),
    path('log-in/', TemplateView.as_view(template_name='index.html')),
    path('to-do-lists/', TemplateView.as_view(template_name='index.html')),
    path('to-do-lists/<slug:slug>/', TemplateView.as_view(template_name='index.html')),
    # api urls
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls')),
    re_path(r'^api/v1/auth/', include('djoser.urls.authtoken')),
    path('api/v1/', include('todo.urls')),

]
