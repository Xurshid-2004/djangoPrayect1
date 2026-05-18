from django.db import models

# Create your models here.

class Category(models.Model):
    title=models.CharField(max_length=21212)
    def __str__(self):
        return self.title

class Article(models.Model):
    title=models.CharField(max_length=121)
    description=models.TextField(max_length=121)
    image=models.ImageField(upload_to='articles/')
    view=models.IntegerField()
    ctreated_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
















 