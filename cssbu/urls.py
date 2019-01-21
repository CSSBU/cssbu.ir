from django.contrib import admin
from django.urls import path, include

from django.views.generic.base import TemplateView

urlpatterns = [
	path('admin/', admin.site.urls),

	path('', TemplateView.as_view(template_name='index.html'), name='main'),

	path('about', TemplateView.as_view(template_name='about-us.html'), name='about-us', kwargs={'title': 'درباره ی ما'}),
	path('contact', TemplateView.as_view(template_name='contact-us.html'), name='contact-us', kwargs={'title': 'ارتباط با ما'}),

	path('contests', TemplateView.as_view(template_name='contests.html'), name='contests', kwargs={'title': 'مسابقات'}),
	path('gatherings', TemplateView.as_view(template_name='gatherings.html'), name='gatherings', kwargs={'title': 'دورهمی ها'}),
	path('celebrations', TemplateView.as_view(template_name='celebrations.html'), name='celebrations', kwargs={'title': 'جشن ها'}),

	path('pardazeh/', include('pardazeh.urls')),
	path('activities/', include('activities.urls')),
]
