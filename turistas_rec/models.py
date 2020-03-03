from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20,null=False) 
    def __str__(self):
        return str(self.name)

class Place(models.Model):
    name = models.CharField(max_length=20,null=False)
    specification = models.ManyToManyField('Category',related_name='description')
    longitude = models.DecimalField(max_digits=30, decimal_places=6)
    latitude = models.DecimalField(max_digits=30, decimal_places=6)
    howtoreach = models.CharField(default='nil',max_length=100,null=False)
    ratings = models.IntegerField(default=0)
    visited = models.IntegerField(default=0)
    view = models.CharField(default='nil',max_length=100,null=False)
    description = models.CharField(default='nil',max_length=100,null=False)
    image = models.ImageField(default='images/sample.jpg',upload_to=None, height_field=None, width_field=None, max_length=100)


    def __str__(self):
        return str(self.name)


class Review(models.Model):
    place_ref = models.ForeignKey('Place',on_delete=models.CASCADE,null=True)
    review_text = models.CharField(max_length=400)
    def __str__(self):
        return str(self.place_ref.name+" : "+self.review_text)
