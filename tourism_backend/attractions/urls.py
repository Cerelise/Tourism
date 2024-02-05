from django.urls import path
from . import views

urlpatterns = [ 
    path('list',views.AttractionListView.as_view()),
    path('detail/<uuid:pk>',views.AttractionManager.as_view()),
    path('article/list',views.AttrArticleListView.as_view()),
    path('article/detail/<uuid:pk>',views.AttrArticleManager.as_view()),
    path('scentic/',views.getScentic,name='get_scentic_list'),
]