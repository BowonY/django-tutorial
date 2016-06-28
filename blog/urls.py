from django.conf.urls import url
from . import views

# mysite/urls.py 에서 url(r'', include('blog.urls')) 했어서
# Django will redirect everything that comes into htp://127.0.0.1:8000/
# to blog.urls and look for further instructions there.

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^category/([0-9]+)/$', views.category, name='category'),
    url(r'^posts/$', views.post_list, name='post_list'),
    url(r'^posts/([0-9]+)/$', views.post_view, name='post_view'),
    url(r'^write/$', views.write_post, name='write_post'),
]
