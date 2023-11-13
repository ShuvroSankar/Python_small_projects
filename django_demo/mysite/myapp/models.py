from django.db import models


# Create your models here.
class Book(models.Model):
    def __self__(self):
        return self.name

    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.IntegerField()
    book_image = models.ImageField(default="default.jpg", upload_to="book_images/")
