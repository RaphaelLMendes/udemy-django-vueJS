from django.db.models.query import QuerySet
from rest_framework import generics, permissions
from rest_framework.generics import get_object_or_404

from ebooks.models import Ebooks, Review
from .serializers import EbookSerializer, ReviewSerializer
from .pagination import SmallSetPagination


class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebooks.objects.all().order_by("-id")
    serializer_class = EbookSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = SmallSetPagination


class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebooks.objects.all()
    serializer_class = EbookSerializer

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebooks, pk=ebook_pk)

        review_author = self.request.user

        serializer.save(ebook=ebook, review_author=review_author)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



# class EbookListCreateAPIView(   mixins.ListModelMixin, 
#                                 mixins.CreateModelMixin ,
#                                 generics.GenericAPIView):
#     queryset = Ebooks.objects.all()
#     serializer_class = EbookSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)