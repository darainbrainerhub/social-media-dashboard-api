from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Like
from .serializers import LikeSerializer, CommentSerializer

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        post_id = kwargs.get('pk')
        action = request.data.get('action')

        existing_like = Like.objects.filter(user=user, post_id=post_id).first()

        if existing_like:
            if existing_like.action == action:
                existing_like.delete()
                return Response({"message": f"Successfully undone {action}.", "post": post_id}, status=status.HTTP_200_OK)
            else:
                existing_like.action = action
                existing_like.save()
                return Response({"message": f"Successfully updated action to {action}.", "post": post_id}, status=status.HTTP_200_OK)
        else:
            data = {
                'user': user.id,
                'post': post_id,
                'action': action
            }
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            like_instance = serializer.save(user=user, post_id=post_id)
            return Response({"post": like_instance.post_id, "action": like_instance.action}, status=status.HTTP_201_CREATED)
        
class CommentCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        post_id = kwargs.get('pk')
        comment = request.data.get('comment')

        data = {
            'user': user.id,
            'post': post_id,
            'comment': comment
        }  

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        comment_instance = serializer.save(user=user, post_id=post_id)
        return Response({"comment": comment_instance.comment}, status=status.HTTP_201_CREATED)
    

