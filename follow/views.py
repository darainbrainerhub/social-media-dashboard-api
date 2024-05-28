from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Follow
from .serializers import FollowSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class FollowToggleView(generics.GenericAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        follower = request.user
        following_id = kwargs.get('user_id')
        try:
            following = User.objects.get(id=following_id)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if follower == following:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        follow_instance, created = Follow.objects.get_or_create(follower=follower, following=following)

        if not created:
            follow_instance.delete()
            return Response({"detail": "Successfully unfollowed."}, status=status.HTTP_200_OK)

        return Response({"detail": "Successfully followed."}, status=status.HTTP_201_CREATED)


class FollowerCountView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        follower_count = Follow.objects.filter(following=user).count()
        following_count = Follow.objects.filter(follower=user).count()
        return Response({
            "followers": follower_count,
            "following": following_count
        }, status=status.HTTP_200_OK)