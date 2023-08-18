from django.contrib import admin
from .models import Question

# Admin에게 Question 클래스가 admin 인터페이스를 가지고 있다 알림
admin.site.register(Question)

# Register your models here.
