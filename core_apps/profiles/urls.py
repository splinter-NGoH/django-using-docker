from django.urls import path

from .views import (
    FollowUnfollowAPIView,
    get_my_followers,
    UpdateProfile,
    ProfileDetail,
    ProfileList,
)

urlpatterns = [
    path("all/", ProfileList.as_view(), name="all-profiles"),
    path("user/<str:username>/", ProfileDetail.as_view(), name="profile-details"),
    path("update/<str:username>/", UpdateProfile.as_view(), name="profile-update"),
    path("<str:username>/followers/", get_my_followers, name="my-followers"),
    path(
        "<str:username>/follow/",
        FollowUnfollowAPIView.as_view(),
        name="follow-unfollow",
    ),
]
