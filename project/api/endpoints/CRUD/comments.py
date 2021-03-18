from api.models import Comment, Post
from api.serializers import CommentSerializer

from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def read_post_comments(request, pk):
    post_qs = get_object_or_404(Post, pk=pk)
    comments_qs = post_qs.comment_set
    serialized = CommentSerializer(comments_qs, many=True)
    response = {"data": serialized.data}
    return Response(response, status=200)


@api_view(["POST"])
def create_comment(request):
    serialized = CommentSerializer(data=request.data)

    if serialized.is_valid(raise_exception=True):
        serialized.save()
        response = {"data": serialized.data}
        return Response(response, status=201)
    return Response({"message": "Error - not created"}, status=400)


@api_view(["POST"])
def update_comment(request, pk):
    comment_obj = get_object_or_404(Comment, pk=pk)
    serialized = CommentSerializer(
        comment_obj,
        data=request.data,
        partial=True,
    )
    if serialized.is_valid(raise_exception=True):
        serialized.save()
        response = {"data": serialized.data, "message": "All good, updated"}
        return Response(response, status=200)

    return Response({"Error - not updated"}, status=400)


@api_view(["DELETE"])
def delete_comment(request, pk):
    comment_obj = get_object_or_404(Comment, pk=pk)
    if comment_obj.delete()[0] > 0:
        return Response({"message": "All good, deleted"}, status=200)
    return Response({"message": "Error - not deleted"}, status=400)
