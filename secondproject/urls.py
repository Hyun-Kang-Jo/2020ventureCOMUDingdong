"""secondproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('blog/<int:blog_id>/', blog.views.detail, name='detail'),
    path('blog/write/', blog.views.write, name="write"),
    path('blog/send/', blog.views.send, name="send"),
    path('delete/<int:blog_id>/', blog.views.delete, name="delete"),
    path('update/<int:blog_id>/', blog.views.update, name="update"),
    path('updateSend/<int:blog_id>/', blog.views.updateSend, name ="updateSend"),
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
