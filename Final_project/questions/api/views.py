from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.validators import ValidationError
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly

from questions.models import Question, Answer

from .serializers import QuestionSerializer, AnswerSerializer

class QuestionViewset(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by("-created_at")
    serializer_class = QuestionSerializer
    permissions_classes = (IsAuthorOrReadOnly)
    lookup_field = "slug"

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all().order_by("-created_at")
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        request_user = self.request.user
        kwarg_slug = self.kwargs.get("slug")
        question = get_object_or_404(Question, slug=kwarg_slug)
        if question.answers.filter(author=request_user).exists():
            raise ValidationError("you have already answered this question!")
        serializer.save(author=request_user, question=question)

class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permissions_classes = (IsAuthorOrReadOnly)
    lookup_field = "uuid"

class AnswerListAPIView(generics.ListAPIView):
    queryset = Answer.objects.all().order_by("-created_at")
    serializer_class = AnswerSerializer

    def get_queryset(self):

        kwarg_slug = self.kwargs.get("slug")

        return Answer.objects.filter(question__slug=kwarg_slug).order_by("-created_at")
