from django.urls import path
import api.endpoints.CRUD.comments as CV
import api.endpoints.CRUD.posts as PV
import api.endpoints.main as MV

urlpatterns = [
    # comments
    path("comments/create", CV.create_comment),
    path("comments/<int:pk>", CV.read_post_comments),
    path("comments/<int:pk>/update", CV.update_comment),
    path("comments/<int:pk>/delete", CV.delete_comment),
    # posts
    path("posts/", PV.PostEndpoint.as_view()),
    path("posts/<int:pk>", PV.PostDetailedEndpoint.as_view()),
    # main
    path("posts/upvote/<int:pk>", MV.UpvotesEndpoint.as_view()),
    path("test-celery", MV.TestCeleryEndpoint.as_view()),
]
