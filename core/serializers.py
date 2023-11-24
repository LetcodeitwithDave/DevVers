from rest_framework import serializers

from .models import  Post


class PostSerializer(serializers.ModelSerializer):
    """serializers.ModelSeriallizer is by convention in django rest_framework"""
    class Meta:
        model  = Post
        fields = '__all__'