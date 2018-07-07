from django.db import models


class Magazine(models.Model):
	number = models.IntegerField()
	published_date = models.DateField()
	uploaded_date = models.DateField(auto_now=True)

	cover_picture = models.ImageField(upload_to='pardazeh/covers/')
	contents = models.TextField()

	file = models.FileField(upload_to='pardazeh/files')
