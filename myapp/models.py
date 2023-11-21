from django.db import models


BOOK_CHOICE = (
    ('ROMANCE','Romance'),
    ('ADVENTURE', 'Adventure'),
    ('HORROR','Horror'),
    ('SCIENCE FICTION','Science Fiction'),

)
# Create your models here.
class Genredb(models.Model):
    Genre = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True,blank=True)

class Bookdb(models.Model):
    Bookname = models.CharField(max_length=100, null=True, blank=True)
    Authorname = models.CharField(max_length=100, null=True, blank=True)
    Description = models.CharField(max_length=15,choices=BOOK_CHOICE,default='ADVENTURE')
    Priceperday=models.IntegerField(null=True)
    Synopsis=models.TextField(max_length=200)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
