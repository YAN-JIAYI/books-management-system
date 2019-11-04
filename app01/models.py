from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    publish = models.ForeignKey(to='Publish')
    author = models.ManyToManyField(to='Author')

class Publish(models.Model):
    name = models.CharField(max_length=64, unique=True)
    addr = models.CharField(max_length=255)
    # def __str__(self):
    #     return f"出版社{self.name}"


class Author(models.Model):
    name = models.CharField(max_length=32)
    author_detail = models.OneToOneField(to='AuthorDetail')

class AuthorDetail(models.Model):
    phone = models.CharField(max_length=32)






