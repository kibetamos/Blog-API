# The serializer not only transforms data into JSON, it can also specify which fields to include or
# exclude.
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)

        model = Post
