from api.models import Post
from api.serializers import PostSerializer

from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView


class PostEndpoint(APIView):
    def get(self, request):
        post_qs = Post.objects.all()
        serialized = PostSerializer(post_qs, many=True)
        response = {"data": serialized.data}
        return Response(response, status=200)

    def post(self, request):
        serialized = PostSerializer(data=request.data)
        if serialized.is_valid(raise_exception=True):
            serialized.save()
            response = {"data": serialized.data}
            return Response(response, status=201)
        return Response({"message": "Error - not created"}, status=400)


class PostDetailedEndpoint(APIView):
    def get_post(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk):
        post_obj = self.get_post(pk)
        serialized = PostSerializer(post_obj)
        response = {"data": serialized.data}
        return Response(response, status=200)

    def patch(self, request, pk):
        post_obj = self.get_post(pk)
        serialized = PostSerializer(
            post_obj,
            data=request.data,
            partial=True,
        )
        if serialized.is_valid(raise_exception=True):
            serialized.save()
            response = {
                "data": serialized.data,
                "message": "All good, updated",
            }
            return Response(response, status=200)
        return Response({"message": "Error - not updated"}, status=400)

    def delete(self, request, pk):
        post_obj = self.get_post(pk)
        if post_obj.delete()[0] > 0:
            return Response({"message": "All good, deleted"}, status=200)
        return Response({"message": "Error - not deleted"}, status=400)
