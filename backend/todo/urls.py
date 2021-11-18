from django.urls import path, include
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register('todos', views.ToDoView, 'todo')

urlpatterns = [path('api/', include(router.urls))]