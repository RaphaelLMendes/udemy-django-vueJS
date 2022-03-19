from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly

from questions.models import Question

from .serializers import QuestionSerializer

class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer
    permissions_classes = (IsAuthorOrReadOnly)
    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)