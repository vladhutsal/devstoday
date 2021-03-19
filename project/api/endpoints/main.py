from api.models import Post, Like

from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404


class UpvotesEndpoint(APIView):
    def post(self, request, pk: int):
        post_obj = get_object_or_404(Post, pk=pk)
        like_obj = Like.objects.create(post=post_obj)
        like_obj.save()
        response = {"message": f"Post #{post_obj.pk} ve' been liked"}
        return Response(response, status=200)

    def get(self, request, pk: int):
        post_obj = get_object_or_404(Post, pk=pk)
        likes_count = post_obj.like_set.count()
        response = {"data": likes_count}
        return Response(response, status=200)
