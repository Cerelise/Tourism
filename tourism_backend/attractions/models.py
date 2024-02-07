import uuid

from django.db import models

# Create your models here.
class Attraction(models.Model):

    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    # main_pic = models.ImageField(upload_to='attraction')
    # map_pic = models.ImageField(upload_to='attraction_map')
    main_pic = models.CharField(null=True,max_length=500)
    map_pic = models.CharField(null=True,max_length=500)
    about = models.CharField(max_length=50)
    content = models.TextField()
    status = models.SmallIntegerField(default=1) # 是否删除
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title



class AttractionsPicture(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=50)
    desc = models.TextField()
    # picture = models.ImageField(upload_to='attraction_swiper')
    picture = models.CharField(null=True,max_length=500)
    related_attr = models.ForeignKey(Attraction,on_delete=models.SET_NULL,related_name='pictures',null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title

class AttractionsArticle(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=50)
    subTitle = models.CharField(max_length=50)
    content = models.TextField()
    img = models.ImageField(upload_to='article_pic')
    scentic = models.CharField(max_length=50)
    isTop = models.BooleanField(default=False)
    status = models.SmallIntegerField(default=1) # 是否删除
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title

class Paragraph(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    related_article = models.ForeignKey(AttractionsArticle,on_delete=models.SET_NULL,related_name='paragraphs',null=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self) -> str:
        return self.title
    
