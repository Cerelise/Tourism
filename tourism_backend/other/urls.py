from django.urls import path
from . import views

urlpatterns = [
  path('category/list',views.CategoryListView.as_view()),
  path('category/detail/<str:category_id>',views.CategoryManagerView.as_view()),
  path('question/list',views.QuestionsListView.as_view()),
  path('question/add',views.addQuestion,name="add_question"),
  path('question/delete/<uuid:pk>',views.deleteQuestion,name="delete_question"),
  path('notice/list',views.NoticeListView.as_view()),
  path('notice/detail/<uuid:pk>',views.NoticeManagerView.as_view()),
  path('home/list',views.HomeListView.as_view()),
  path('home/detail/<uuid:pk>',views.HomeManagerView.as_view()),
]