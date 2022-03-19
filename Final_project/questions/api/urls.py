from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter

from questions.api import views as qv

router = DefaultRouter()
router.register(r"questions", qv.QuestionViewset)

urlpatterns = [
    path('', include(router.urls) )
]