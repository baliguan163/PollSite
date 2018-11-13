from django.contrib import admin
from .models import Question,Choice
# Register your models here.

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_date', 'question_text']

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]


# 现在还无法看到投票应用，必须先在admin中进行注册，告诉admin站点，请将polls的模型加入站点内，接受站点的管理。
# 打开polls/admin.py文件，加入下面的内容：
# from django.contrib import admin
# from .models import Question
# admin.site.register(Question)


class ChoiceInline(admin.TabularInline): # admin.TabularInline admin.StackedInline
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choice)
#
# 增加显示列    list_display = ('question_text', 'pub_date', 'was_published_recently')
# 增加过滤器    list_filter = ['pub_date']
# 添加搜索栏    search_fields = ['question_text']
