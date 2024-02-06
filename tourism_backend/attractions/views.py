import json

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes

from .serializers import AttractionSerializer,AttractionsArticleSerializer
from .models import Attraction,AttractionsPicture,AttractionsArticle,Paragraph
from .permissions import IsAdminUserOrReadOnly

# Create your views here.

class AttractionListView(APIView):

    permission_classes = [IsAdminUserOrReadOnly]

    def get(self,request):
        attractions = Attraction.objects.filter(status=1)
        # attractions = Attraction.objects.all()
        serializer = AttractionSerializer(attractions,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        
        data = request.data

        title = data['title']
        desc = data['desc']
        main_pic = data['main_pic']
        map_pic = data['map_pic']
        about = data['about']
        content = data['content']

        attr_data = {
          'title':title,
          'desc':desc,
          'main_pic':main_pic,
          'map_pic':map_pic,
          'about':about,
          'content':content,
        }
        attraction = Attraction.objects.create(**attr_data)
        # title=title,desc=desc,main_pic=main_pic,map_pic=map_pic,about=about,content=content

        pictures_data = json.loads(data.get('pictures'))
        # print(pictures_data)
        for picture_data in pictures_data:
            title = picture_data["title"]
            desc = picture_data["desc"]
            # picture = picture_data["picture"]
            related_attr = attraction

            attraction_pic = AttractionsPicture(title=title,desc=desc,related_attr=related_attr)
            attraction_pic.save()

        serializer = AttractionSerializer(attraction,many=False)

        response = {
          'message':'创建成功！',
          'data':serializer.data
        }

        return Response(data=response,status=status.HTTP_201_CREATED)


class AttractionManager(APIView):

      permission_classes = [IsAdminUserOrReadOnly]
      serializer_class = AttractionSerializer

      def get(self,request,pk):
          attr = get_object_or_404(Attraction,id=pk)
          attr_serializer = self.serializer_class(instance=attr)

          return Response(
            {"detail":attr_serializer.data},
            status=status.HTTP_200_OK
          )


      def delete(self,request,pk):
          attr = get_object_or_404(Attraction,id=pk)
          attr.status = 0
          attr.save()

          return Response({"message":"该景点信息已删除！"},status=status.HTTP_200_OK)


class AttrArticleListView(APIView):

    permission_classes = [IsAdminUserOrReadOnly]

    def get(self,request):
        articles = AttractionsArticle.objects.filter(status=1)
        serializer = AttractionsArticleSerializer(articles,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):

        data = request.data

        article_data = {
          "title":data['title'],
          "subTitle":data['subTitle'],
          "content":data['content'],
          "img":data['img'],
          "scentic":data['scentic'],
          "isTop":data['isTop'],
        }

        # article_serializer = AttractionsArticleSerializer(data=article_data)
        article = AttractionsArticle.objects.create(**article_data)

        paragraphs_data = json.loads(data.get('paragraphs'))

        for paragraph in paragraphs_data:
            title = paragraph['title']
            content = paragraph['content']
            related_article = article
            
            article_paragraph = Paragraph(title=title,content=content,related_article=related_article)
            article_paragraph.save()
        
        serializer = AttractionsArticleSerializer(article)

        response = {
            "message":"景点文章创建成功！",
            "detail":serializer.data
        }
        return Response(data=response,status=status.HTTP_201_CREATED)


class AttrArticleManager(APIView):

      permission_classes = [IsAdminUserOrReadOnly]
      serializer_class = AttractionsArticleSerializer

      def get(self,request,pk):
          article = get_object_or_404(AttractionsArticle,id=pk)
          article_serializer = self.serializer_class(instance=article)

          return Response(
            {"detail":article_serializer.data},
            status=status.HTTP_200_OK
          )


      def delete(self,request,pk):
          article = get_object_or_404(AttractionsArticle,id=pk)
          article.status = 0
          article.save()

          return Response({"message":"该景点文章已删除！"},status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes(['IsAdminUserOrReadOnly'])
def getScentic(request):

    article_list = AttractionsArticle.objects.all()

    scentic_list = article_list.values_list('scentic',flat=True)
    
    

    return Response(scentic_list,status=status.HTTP_200_OK)




          


        


      
      


