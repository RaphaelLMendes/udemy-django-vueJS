from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from questions.api import views as qv

router = DefaultRouter()
router.register(r"questions", qv.QuestionViewset)
#router.register(r"answers", qv.AnswerViewset)

urlpatterns = [
    path('', include(router.urls) ),
    path(
        'questions/<slug:slug>/answers', 
        qv.AnswerListAPIView.as_view(), 
        name="answer-list" 
        ),
    path(
        'questions/<slug:slug>/answer', 
        qv.AnswerCreateView.as_view(), 
        name="answer-create" 
        ),
    path(
        'answers/<uuid:uuid>/', 
        qv.AnswerRUDAPIView.as_view(), 
        name="answer-RUD" 
        ),
    
]