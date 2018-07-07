from django.urls import path

from .views import AllMagazineView

urlpatterns = [
	path('', AllMagazineView.as_view(), name='pardazeh'),
]
