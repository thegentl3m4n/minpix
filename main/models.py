from django.db import models
from PIL import Image
import PIL
from django.utils import timezone


# Create your models here.

class IMage(models.Model):
	title = models.CharField(max_length=50)
	image_file = models.ImageField(upload_to='images/')
	date_added = models.DateTimeField(default=timezone.now)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.image_file.path)
		new_width = img.size[0]
		new_height = img.size[1]
		img = img.resize((new_width,new_height), PIL.Image.ANTIALIAS)
		img.save(self.image_file.path)
