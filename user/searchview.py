from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import permissions
from rest_framework import serializers

User = get_user_model()

class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class SearchUserView(generics.ListAPIView):
    serializer_class = UserSearchSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        searched_username = self.request.query_params.get('username', '') 
        return User.objects.filter(username__icontains=searched_username)
