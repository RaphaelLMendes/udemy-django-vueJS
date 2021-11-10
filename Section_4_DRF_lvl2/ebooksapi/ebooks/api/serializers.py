from django.db.models import fields
from django.db.models.query_utils import select_related_descend
from rest_framework import serializers
from ebooks.models import Ebooks, Review

class ReviewSerializer(serializers.ModelSerializer):
    
    review_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('ebook',)
        #fields = "__all__"


class EbookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Ebooks
        fields = "__all__"