from django.contrib import admin
from django.http import HttpResponse, Http404  # Http404 추가
from django.urls import path
from django.shortcuts import render  # 여기서 한 번만 import

# 영화 데이터
movie_list = [
    {'title': '파묘', 'director': '정재현'},
    {'title': '윙카', 'director': '폴 킹'},
    {'title': '듄: 파트2', 'director': '드니 빌뇌브'},
    {'title': '시민덕희', 'director': '박영주'},
]

# 뷰 함수들
def index(request):
    return HttpResponse('<h1>hello</h1>')

def book_list(request):
    book_test = ''
    for i in range(0, 10):
        book_test += f'book {i}<br>'
    return HttpResponse(book_test)

def book(request, num):
    return HttpResponse(f'book {num}번 페이지입니다.')

def languge(request, lang):
    return HttpResponse(f'<h1>{lang} 언어 페이지입니다.</h1>')  # 닫는 태그 </h1> 추가

def movies(request):
    return render(request, template_name='movies.html', context={'movie_list': movie_list})

def movie_detail(request, index):
    if index > len(movie_list) - 1:
        raise Http404  # 제대로 import 필요
    movie = movie_list[index]
    context = {'movie': movie}
    return render(request, template_name='movie.html', context=context)

def gugu(request, num):
    context = {
        'num': num,
        'results' : [num*i for i in range(1,10)]
    }

    return render(request, template_name= 'gugu.html', context=context)

# URL 매핑
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('book_list/', book_list),
    path('book_list/<int:num>/', book),
    path('language/<str:lang>/', languge),
    path('movie/', movies),
    path('movie/<int:index>/', movie_detail),
    path('gugu/<int:num>/', gugu),
]