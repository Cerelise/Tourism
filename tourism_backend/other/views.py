import json

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import QandA,Category,notice,HomeInfo
from .serializers import QandASerializer,CategorySerializer,NoticeSerializer,HomeSerializer

# Create your views here.
class CategoryListView(APIView):

    def get(self,request):
        cateories = Category.objects.filter(status=1)
        serializer = CategorySerializer(cateories,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)
  
    def post(self,request):

        data = request.data

        title = data['title']

        category = Category.objects.create(title=title)

        response = {
          'message':'分类创建成功',
        }

        return Response(response,status=status.HTTP_201_CREATED)

class CategoryManagerView(APIView):

    def get(request,pk):
        
        category = get_object_or_404(Category,id=pk)
        questions = QandA.objects.filter(category=category)

        serializer = QandASerializer(questions,many=True)
        
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def delete(request,pk):
        
        category = get_object_or_404(Category,id=pk)
        category.status = 0
        category.save()

        questions = QandA.objects.filter(category=category)

        for question in questions:
            question.status = 0
            question.save()
        
        return Response({"message":"该分类已删除！"},status=status.HTTP_200_OK)

        


class QuestionsListView(APIView):

    def get(self,request):
        questions = QandA.objects.filter(status=1)
        serializer = QandASerializer(questions,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)



@api_view(['POST'])
def addQuestion(request,pk):

    data = request.data

    question_data = {
        "question":data['question'],
        "answer":data['answer'],
        "category":pk
    }

    question_serializer = QandASerializer(data=question_data)

    if question_serializer.is_valid():
            
        question_serializer.save()

        response = {
          "message":"问答创建成功！",
          "datail":question_serializer.data
        }

        return Response(data=response,status=status.HTTP_201_CREATED)
    return Response(data=question_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteQuestion(request,pk):
    
    question = get_object_or_404(QandA,id=pk)

    question.status = 0
    question.save()

    return Response({"message":"该问答已经删除！"},status=status.HTTP_200_OK)


# 公告
class NoticeListView(APIView):
    
    def get(self,request):
        
        notice_list = notice.objects.filter(status=1)
        serializer = NoticeSerializer(notice_list,many=True)
        
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):

        data = request.data

        notice_data = {
          'title':data['title'],
          'content':data['content']
        }

        notice_serializer = NoticeSerializer(data=notice_data)

        if notice_serializer.is_valid():
            notice_serializer.save()

            response = {
              "message":"公告创建成功！",
              "detail":notice_serializer.data
            }
            return Response(data=response,status=status.HTTP_200_OK)


class NoticeManagerView(APIView):

    serializer_class = NoticeSerializer
    
    def get(self,request,pk):

        notice_obj = get_object_or_404(notice,id=pk)

        serializer = self.serializer_class(instance=notice_obj)

        return Response(
            {"detail":serializer.data},
            status=status.HTTP_200_OK
        )
    
    def delete(self,request,pk):
        notice_obj = get_object_or_404(notice,id=pk)
        notice_obj.status = 0
        notice_obj.save()

        return Response({"message":"该公告已删除！"},status=status.HTTP_200_OK)

# 主页
class HomeListView(APIView):
    
    def get(self,request):

        home_list = HomeInfo.objects.filter(status=1)
        serializer = HomeSerializer(home_list,many=True)

        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def post(self,request):

        data = request.data

        home_data = {
          'title':data['title'],
          'desc':data['desc'],
          'picture':data['picture']
        }

        home_serialzer = HomeSerializer(data=home_data)

        if home_serialzer.is_valid():
            home_serialzer.save()

            response = {
              "message":"主页信息已创建",
              "datail":home_serialzer.data
            }

            return Response(data=response,status=status.HTTP_201_CREATED)


class HomeManagerView(APIView):
  
    serializer_class = HomeSerializer
    
    def get(self,request,pk):

        home = get_object_or_404(HomeInfo,id=pk)

        serializer = self.serializer_class(instance=home)

        return Response(
            {"detail":serializer.data},
            status=status.HTTP_200_OK
        )
    
    def delete(self,request,pk):
        home = get_object_or_404(HomeInfo,id=pk)
        home.status = 0
        home.save()

        return Response({"message":"该主页内容已删除！"},status=status.HTTP_200_OK)










