# The serializer not only transforms data into JSON, it can also specify which fields to include or
# exclude.

from pyexpat import model
from attr import fields
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'created_at',)
        model = Post
