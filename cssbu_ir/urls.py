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
