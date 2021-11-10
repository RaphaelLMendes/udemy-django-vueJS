from django.contrib.auth.models import Permission
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile
from .serializers import ProfileSerializer

class ProfileListAPIView(generics.ListAPIView):
    
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Profile.objects.all().order_by('-id')
        username = self.request.query_params.get("username", None)
        if username is not None:
            queryset = Profile.objects.filter(user__username=username)
        return queryset