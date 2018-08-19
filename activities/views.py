from django.views.generic.list import ListView

from .models import *


class AllSeminarView(ListView):
	model = Seminar
	template_name = 'seminars.html'
