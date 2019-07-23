from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects    #모델로부터 객채목록을 전달받을 수 있게된다. 이 객체 목록 : 쿼리셋  # 쿼리셋 정렬/기능 표시방법 : 메소드
    return render(request, 'home.html', {'blogs':blogs})

    # 쿼리셋과 메소드의 형식
    # 모델이름.쿼리셋(objects).메소드


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)    #blog_id번째 객체
    return render(request, 'detail.html', {'blog':blog_detail})
            
def new(request):   #new.html 띄워주는 함수
    return render(request, 'new.html')

def create(request):    #입력받은 내용을 데베에 넣어주는 함수
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date = timezone.datetime.now() #입력시간
    blog.save() #쿼리셋 메소드  객체.delete() ->객체 내용을 지워라
    return redirect('/blog/'+str(blog.id))  
    # redirect(URL) -> URL에 어떤 URL이든 넣을 수 있음. / 프로젝트 외 url가능
    # render함수는 프로그램 내 페이지 이동이 주됨.
    # 이 (URL)로 넘기세요, str 문자열 형변환
    # 데이터가 처리되고 save된다음에 url로 이동됨.