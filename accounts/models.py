from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class Customer(models.Model):
    SEXE=(('Femme','Femme'),('Homme','Homme'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sexe=models.CharField(null=True,choices=SEXE,max_length=10)
    phone = models.CharField(blank=True, max_length=20,null=True)
    address = models.CharField(blank=True, max_length=150,null=True)
    city = models.CharField(blank=True, max_length=20,null=True)
    country = models.CharField(blank=True, max_length=50,null=True)
    image = models.ImageField(blank=True,default="person.png",null=True)
    zipcode=models.IntegerField(default=0,null=True)
    bio=models.TextField(null=True)
    #language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True,blank=True)
    #currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True,blank=True)


    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'