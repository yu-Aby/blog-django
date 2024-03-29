"""web URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

from rest_framework.documentation import include_docs_urls
from blog.views import ArticleListViewSet,TagListViewSet,CategoryListViewSet
from rest_framework.routers import DefaultRouter

import xadmin

router = DefaultRouter()
router.register(r'article', ArticleListViewSet)
router.register(r'tag', TagListViewSet)
router.register(r'category', CategoryListViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'mdeditor/', include('mdeditor.urls')),
    url('', include(router.urls)),
    url(r'docs/',include_docs_urls(title="_blog")),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url(r'media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
]



