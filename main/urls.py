from django.urls import path
from . import views

#ルーティング情報を列挙する
urlpatterns = [
    path('',views.index, name ='index'),
    path('temp',views.temp, name = 'temp'),
    path('list',views.list, name = 'list'),
    path('iftag',views.iftag, name = 'iftag'),
    path('yesno',views.yesno, name = 'yesno'),
    path('firstof',views.firstof, name = 'firstof'),
    path('forloop',views.forloop, name = 'forloop'),
    path('fortag',views.fortag, name = 'fortag'),
    path('ifchanged',views.ifchanged, name = 'ifchanged'),
    path('regroup',views.regroup, name = 'regroup'),
    path('cycle',views.cycle, name = 'cycle'),
    path('master',views.master, name = 'master'),
    path('include',views.include, name = 'include'),
    path('static',views.static, name = 'static'),
    path('slice',views.slice, name = 'slice'),

]