from django.db import models



# Create your models here.
class Member(models.Model):
    
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField()
    email = models.EmailField(max_length=200)#changes
    web = models.CharField(max_length=200)
    age = models.IntegerField()
    

    def __str__(self):
        return self.first_name

    
    

