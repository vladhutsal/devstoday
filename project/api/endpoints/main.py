from api.models import Post
from api.serializers import PostSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404


@api_view(["PATCH"])
def upvote_post(request, pk):
    post_obj = get_object_or_404(Post, pk=pk)
    post_obj.upvotes += 1
    post_obj.save()
    serialized = PostSerializer(post_obj)
    response = {"data": serialized.data}
    return Response(response, status=200)
