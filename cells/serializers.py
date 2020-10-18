from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Cell


class CellSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('column', 'row', 'value')
        model = Cell
        validators = [
            UniqueTogetherValidator(
                queryset=Cell.objects.all(),
                fields=['column', 'row']
            )
        ]
