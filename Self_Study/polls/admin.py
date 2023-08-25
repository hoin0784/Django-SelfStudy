from django.contrib import admin
from .models import Choice, Question


# Choice 객체를 시스템에 추가하는 방법은 비효율적이므로,
# Question 객체를 생성할 때 여러 개의 Choices를 직접 추가 방법이 더 효율적

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
  search_fields = ["question_text"]                   # Using %Like query
  fieldsets = [
        (None,               {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),]
  inlines = [ChoiceInline]
  list_display = ["question_text", "pub_date", "was_published_recently"]
  list_filter = ["pub_date"]


admin.site.register(Question, QuestionAdmin)
