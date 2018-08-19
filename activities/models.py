from django.db import models


class Seminar(models.Model):
	created_date = models.DateTimeField(auto_now_add=True, editable=False)

	title = models.CharField(max_length=100)
	poster = models.ImageField(upload_to='activities/seminars/')
	short_description = models.CharField(max_length=255)
	description = models.TextField()
