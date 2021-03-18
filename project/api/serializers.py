from rest_framework import serializers
from .models import Post, Comment, Like


class PostSerializer(serializers.ModelSerializer):
    upvotes = serializers.SerializerMethodField("get_upvotes")
    class Meta:
        model = Post
        fields = ("pk", "title", "link", "author_name", "upvotes", "creation_date")

    def get_upvotes(self, obj):
        return obj.like_set.count()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("pk", "post", "author_name", "content", "creation_date")
