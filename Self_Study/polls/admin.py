from django.contrib import admin
from .models import Question, Choice

# Admin에게 Question 클래스가 admin 인터페이스를 가지고 있다 알림
admin.site.register(Question)
admin.site.register(Choice)
# Register your models here.
