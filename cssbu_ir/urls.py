"""cssbu_ir URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from django.views.generic.base import TemplateView

urlpatterns = [
	path('admin/', admin.site.urls),

	path('', TemplateView.as_view(template_name='index.html'), name='main'),

	path('about', TemplateView.as_view(template_name='about-us.html'), name='about-us'),
	path('contact', TemplateView.as_view(template_name='contact-us.html'), name='contact-us'),

	path('contests', TemplateView.as_view(template_name='contests.html'), name='contests'),
	path('gatherings', TemplateView.as_view(template_name='gatherings.html'), name='gatherings'),
	path('celebrations', TemplateView.as_view(template_name='celebrations.html'), name='celebrations'),
	path('seminars', TemplateView.as_view(template_name='seminars.html'), name='seminars'),

	path('pardazeh/', include('pardazeh.urls'))
]
