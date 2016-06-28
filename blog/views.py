from django.shortcuts import render, redirect
from blog.models import Post
from blog.forms import PostForm
from django.utils import timezone

# Create your views here.
def home(request):
    return render(request, 'blog/home.html', {})

def post_view(request, num):
    # 자동으로 /에 따라 파라미터 나눠보내줌.
    # posts/1/이면 num=1자동으로
    p = Post.objects.get(id=num)
    title = p.title
    text = p.text
    # post.html에 {{ title }} 이라고 된 부분을 p.title이 채움
    return render(request, 'blog/post_view.html',
            {'title': title, 'text': text})

def post_list(request):
    # render (put together) my template blog/post_list.html
    # returns a HttpResponse
    latest_post_list = Post.objects.order_by('-created_date')[:5]
    context = {'latest_post_list': latest_post_list}
    return render(request, 'blog/post_list.html', context)

def write_post(request):
    # create model and save
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # redirect to post list after submitting
            return redirect('/posts/')
    else:
        form = PostForm()
    return render(request, 'blog/write_post.html', {'form': form})



# TODO: 카테고리 생성후 다시 작업하기
def category(request, num):
    c = Post.objects.get(id=num)
    name = c.name

    #posts = Post.objects.get(category=num)
    return render(request, 'blog/category.html', {})
