from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^messageRead/$', views.messageRead, name='messageRead'),
    path('message_delete/<int:pk>', views.message_delete, name='message_delete'),
    path('admin/eligblityUser/', views.eligblityUser, name='eligblityUser'),
    path('admin/existuser/', views.existuser, name='existuser'),
    path('admin/user/edit/<int:pk>', views.user_edit, name='user_edit'),
    path('user_edit/<int:pk>', views.user_edit, name='user_edit'),
    url(r'^edituserData/$', views.edituserData, name='edituserData'),
    path('user_delete/<int:pk>', views.user_delete, name='user_delete'),
]