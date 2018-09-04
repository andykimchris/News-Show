# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from newsapi import NewsApiClient
import json
from .forms import NewsLetterForm
from django.http import HttpResponse, Http404,HttpResponseRedirect

newsapi = NewsApiClient(api_key='d0201ebca1904f039ecf37e06ea71bb3')

# Create your views here.
def sources(request):

    global newsapi
    sources = newsapi.get_sources(
                                                                language='en',
                                                                country='us'
                                                )

    sources_articles = sources['sources']

    context = {
        'sources_articles': sources_articles
            }

    return render(request, 'sources.html', context)

@login_required(login_url='/accounts/login/')
def articles(request):

    global newsapi
    top_headlines = newsapi.get_top_headlines(
                                            country='us',
                                          language='en',
                                       )

    top_headlines_articles  = top_headlines['articles']

    context = {
        'top_headlines': top_headlines_articles,
        }


    return render(request, 'articles.html', context)

def news_today(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
             name = form.cleaned_data['your_name']
             email = form.cleaned_data['email']
             recipient = NewsLetterRecipients(name = name,email =email)
             recipient.save()
             HttpResponseRedirect('news_today')
      
    return render(request, 'email/newsletter,html', {"date": date,"news":news,"form":form})