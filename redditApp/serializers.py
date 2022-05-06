# serializers
from rest_framework import serializers
from redditApp.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        post = Post
        fields = ('')