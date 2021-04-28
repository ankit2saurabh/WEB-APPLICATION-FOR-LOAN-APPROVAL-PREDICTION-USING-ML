from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('news_detail/<int:id>', views.news_detail, name='news_detail'),
    path('panel/news/list', views.news_list, name='news_list'),
    path('panel/news/add', views.add_news, name='add_news'),
    path('news_delete/<int:pk>', views.news_delete, name='news_delete'),
    path('news_edit/<int:pk>', views.news_edit, name='news_edit'),
    path('panel/news/edit/<int:pk>', views.news_edit, name='news_edit'),
    url(r'^editData/$', views.editData, name='editData'),
]