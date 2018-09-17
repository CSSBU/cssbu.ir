from django.views.generic.list import ListView

from .models import Magazine


class AllMagazineView(ListView):
	model = Magazine
	template_name = 'pardazeh/pardazeh.html'

	def get_queryset(self):
		return Magazine.objects.all().order_by('-number')
