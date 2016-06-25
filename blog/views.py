from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/home.html', {})

def post_list(request):
    # render (put together) my template blog/post_list.html
    # returns a HttpResponse
    return render(request, 'blog/post_list.html', {})
