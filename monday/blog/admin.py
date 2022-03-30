from xml.etree.ElementTree import Comment
from django.contrib import admin
from.models import Article, Comment


admin.site.register(Article)
admin.site.register(Comment)
