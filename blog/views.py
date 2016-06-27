from django.shortcuts import render
from blog.models import Post

# Create your views here.
def home(request):
    return render(request, 'blog/home.html', {})

def posts(request, num):
    # 자동으로 /에 따라 파라미터 나눠보내줌.
    # posts/1/이면 num=1자동으로
    p = Post.objects.get(post_id=num)
    title = p.title
    # post.html에 {{ title }} 이라고 된 부분을 p.title이 채움
    return render(request, 'blog/post.html', {'title': title})

def post_list(request):
    # render (put together) my template blog/post_list.html
    # returns a HttpResponse
    return render(request, 'blog/post_list.html', {})
