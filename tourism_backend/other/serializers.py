from rest_framework import serializers
from .models import Category,QandA,HomeInfo,notice


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id','title','created_at')


class QandASerializer(serializers.ModelSerializer):

    class Meta:
       model = QandA
       fields = ('id','question','answer','created_at','category')


class NoticeSerializer(serializers.ModelSerializer):

    class Meta:
        model = notice
        fields = "__all__"

class HomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = HomeInfo
        fields = "__all__"
    