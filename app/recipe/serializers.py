"""
Serializers for recipe API
"""

from rest_framework import serializers
from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipe model"""

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'description', 'price', 'link')
        read_only_fields = ('id',)
