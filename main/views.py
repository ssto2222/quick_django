from django.shortcuts import render
from django.http import  HttpResponse
from .models import Book
import random
import datetime

# Create your views here.
def index(request):
    pass

def temp(request):
    context = {
        'msg' : 'Hello, world!'
    }

    return render(request,'main/temp.html',context)

def list(request):
    #全ての書籍情報を取得
    books = Book.objects.all()
    return render(request, 'main/list.html',{
        'books':books
    })

def iftag(request):
    return render(request, 'main/iftag.html',{
        #0~100の乱数を生成
        'random':random.randint(0, 100)
    })

#条件による出力がごく短い場合のyesnoフィルター
def yesno(request):
    return render(request,'main/yesno.html',{
        'flag':None
    
    })

def firstof(request):
    return render(request,'main/firstof.html',{
        'a':'おはようございます！',
        'b':'こんにちは！',
        'c':'こんばんは！'
    })

def forloop(request):
    return render(request,'main/forloop.html',{
        'weeks':['月','火','水','木','金','土','日']
    })

def forempty(request):
    return render(request,'main/forempty.html',{
       # 'members':['鈴木太郎','田中花子','高橋是清']
    })

def fortag(request):
    return render(request,'main/fortag.html',{
       'n': 10
    })

def ifchanged(request):
    return render(request,'main/ifchanged.html',{
       'schedule': [
           (10,'A企画反省会'),
           (10,'B書籍脱稿'),
           (15,'WINGS定例会議'),
           (30,'C企画打ち合わせ'),
       ]
    })

def regroup(request):
    return render(request,'main/regroup.html',{
       'members': [
         {'name':'鈴木　太郎','sex':'男','birth':'1980-12-23'},
         {'name':'鈴木　花子','sex':'女','birth':'1978-06-11'},
         {'name':'鈴木　宗子','sex':'女','birth':'1995-03-22'},
         {'name':'鈴木　美子','sex':'女','birth':'2001-10-05'},
         {'name':'鈴木　重四郎','sex':'男','birth':'2005-06-01'},
       ]
    })

def cycle(request):
    return render(request,'main/cycle.html',{
       'members': [
         {'name':'鈴木　太郎','sex':'男','birth':'1980-12-23'},
         {'name':'鈴木　花子','sex':'女','birth':'1978-06-11'},
         {'name':'鈴木　宗子','sex':'女','birth':'1995-03-22'},
         {'name':'鈴木　美子','sex':'女','birth':'2001-10-05'},
       ]
    })

def master(request):
    return render(request,'main/master.html',{
       'msg': 'こんにちは、世界！',
    })


def include(request):
    #ビュー変数name/currentを準備
    return render(request,'main/include.html',{
        'name':'鈴木',
        'current':datetime.datetime.now(),
    })

def static(request):
    #ビュー変数name/currentを準備
    return render(request,'main/static.html',{
        
    })

def slice(request):
    return render(request,'main/slice.html',{
        'data':['い','ろ','は','に','ほ','へ']
    })