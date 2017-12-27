# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.




def index(request):
    # article = models.Article.objects.get(pk=1)
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})

def article_edit_page(request):
    return render(request, 'blog/article_edit_page.html')