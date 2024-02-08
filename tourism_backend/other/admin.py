from django.contrib import admin
from .models import Category,QandA,notice,HomeInfo,Visitation
# Register your models here.


admin.site.register(Category)
admin.site.register(QandA)
admin.site.register(notice)
admin.site.register(HomeInfo)
admin.site.register(Visitation)