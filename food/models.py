from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name
    
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://static.vecteezy.com/system/resources/previews/003/170/825/original/isolated-food-plate-fork-and-spoon-design-free-vector.jpg" )

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    
