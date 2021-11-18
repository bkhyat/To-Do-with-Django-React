from rest_framework import viewsets
from todo.models import ToDo
from todo.serializers import ToDoSerializer


class ToDoView(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
