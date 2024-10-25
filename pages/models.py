from django.db import models



class Menu(models.Model):
    name = models.CharField(max_length=50)
    price =models.IntegerField()
    surat = models.ImageField(upload_to="static/images")
    diccription = models.TextField()
    quantify = models.IntegerField()
    category = models.CharField( max_length=50,default='Zaftra')
    
    def __str__(self):
        return self.name