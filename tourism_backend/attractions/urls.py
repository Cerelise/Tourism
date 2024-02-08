from django.urls import path
from . import views

urlpatterns = [ 
    path('picture',views.uploadAttractionPhoto,name="upload_picture"),
    path('list',views.AttractionListView.as_view()),
    path('detail/<uuid:pk>',views.AttractionManager.as_view()),
    path('article/list',views.AttrArticleListView.as_view()),
    path('article/detail/<uuid:pk>',views.AttrArticleManager.as_view()),
    path('scentic/',views.getScentic,name='get_scentic_list'),
    path('article/search/<str:keyword>',views.AttractionArticleFilterView.as_view()),
    path('home',views.getIndex,name="get_home_page"),
]