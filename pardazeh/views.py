from django.views.generic.list import ListView

from .models import Magazine


class AllMagazineView(ListView):
	model = Magazine
	template_name = 'pardazeh/pardazeh.html'
