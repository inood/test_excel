from rest_framework import viewsets

from .serializers import CellSerializer
from .models import Cell


class CellViewSet(viewsets.ModelViewSet):
    queryset = Cell.objects.all()
    serializer_class = CellSerializer



