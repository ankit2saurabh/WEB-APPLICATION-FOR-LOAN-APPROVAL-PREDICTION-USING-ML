from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^services/$', views.services, name='services'),
    url(r'^ourteam/$', views.ourteam, name='ourteam'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contacts, name='contacts'),
    url(r'^contactus/$', views.cont, name='contactus'),
    url(r'^maintainence/$', views.maintainence, name='maintainence'),
    url(r'^panel/$', views.panel, name='panel'),
    url(r'^checkStatus/$', views.checkStatus, name='checkStatus'),
    url(r'^check/$', views.check_detail, name='check_detail'),
    url(r'^error/$', views.error, name='error'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^checklogin/$', views.userlogin, name='checklogin'),
    url(r'^randomNumberOTP/$', views.randomNumberOTP, name='randomNumberOTP'),
    url(r'^changePassword/$', views.changePassword, name='changePassword'),
    url(r'^forgetPassword/$', views.forgetPassword, name='forgetPassword'),
    url(r'^forgetPassword2/$', views.forgetPassword2, name='forgetPassword2'),
    url(r'^logout/$', views.userlogout, name='logout'),
    url(r'^login/$', views.userloginpage, name='login'),
    url(r'^checkloan/$', views.checkloan, name='checkloan'),
    url(r'^status/$', views.status, name='status'),
    url(r'^adminUser/$', views.adminUser, name='adminUser'),
]