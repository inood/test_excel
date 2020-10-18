from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from .serializers import CellSerializer
from .models import Cell


class CellViewSet(viewsets.ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer



