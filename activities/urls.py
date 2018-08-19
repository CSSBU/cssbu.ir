from django.urls import path

from .views import AllSeminarView

urlpatterns = [
	path('seminars', AllSeminarView.as_view(), name='seminars', kwargs={'title': 'سمینار ها و کارگاه ها'}),
]
