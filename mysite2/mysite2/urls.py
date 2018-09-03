"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from zsdlove import views
from mysite2 import  settings
import os
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'index/',views.index),
    url(r'login/',views.login),
    url(r'add/',views.add),
    url(r'delete_opt',views.delete),
    url(r'^blog/$',views.blogindex),
    url(r'detail_blog',views.article_detail),
    url(r'ueditor/',include('DjangoUeditor.urls')),
    url(r'^comment.html$',views.comment)
]
if settings.DEBUG:
    media_root = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=media_root)

