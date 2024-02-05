from rest_framework import serializers
from .models import Attraction,AttractionsPicture,AttractionsArticle,Paragraph


class AttractionsPicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttractionsPicture
        fields = ('id', 'title', 'desc', 'created_at')

class AttractionSerializer(serializers.ModelSerializer):
    pictures = AttractionsPicSerializer(many=True, read_only=True)

    class Meta:
        model = Attraction
        fields = ('id', 'title', 'desc', 'main_pic', 'map_pic', 'about' ,'content', 'created_at', 'pictures')


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ('id','title','content','created_at')

class AttractionsArticleSerializer(serializers.ModelSerializer):
    paragraphs = ParagraphSerializer(many=True,read_only=True)

    class Meta:
        model = AttractionsArticle
        fields = ('id','title','subTitle','content','img','scentic','isTop','created_at','paragraphs')
