import uuid

from django.db import models

# Create your models here.
class HomeInfo(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    picture = models.ImageField(upload_to='home')
    status = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class notice(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=50)
    status = models.SmallIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

class QandA(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    question = models.CharField(max_length=100)
    answer = models.TextField()
    status = models.SmallIntegerField(default=1)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,related_name='categories',null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title