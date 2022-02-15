# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from newsapi import NewsApiClient
from .forms import NewsLetterForm
from django.http import HttpResponseRedirect
from .utils import get_top_headlines, get_top_sources

newsapi = NewsApiClient(api_key='d0201ebca1904f039ecf37e06ea71bb3')


def sources(request):

    global newsapi
    sources = newsapi.get_sources(language='en')
    sources_articles = sources['sources']

    top_headlines = newsapi.get_top_headlines(
        language='en',
        sources='abc-news,ars-technica,associated-press,axios,bbc-news,bbc-sport,bleacher-report,bloomberg,breitbart-news,business-insider,business-insider-uk,buzzfeed,cbc-news,cbs-news,cnn,crypto-coins-news,engadget,entertainment-weekly,espn,espn-cric-info,financial-post,football-italia,fortune,four-four-two,fox-news,fox-sports,google-news,google-news-au,google-news-ca,google-news-in,google-news-uk,hacker-news,ign,independent,mashable,medical-news-today,msnbc,mtv-news,mtv-news-uk,national-geographic,national-review,nbc-news,news24,new-scientist,news-com-au,newsweek,new-york-magazine,next-big-future,nfl-news,nhl-news,politico,polygon,recode,reddit-r-all,reuters,rte,talksport,techcrunch,techradar,the-american-conservative,the-globe-and-mail,the-hill,the-hindu,the-huffington-post,the-irish-times,the-jerusalem-post,the-lad-bible,the-next-web,the-sport-bible,the-times-of-india,the-verge,the-wall-street-journal,the-washington-post,the-washington-times,time,usa-today,vice-news,wired'
    )

    top_headlines_articles = top_headlines['articles']

    headlines = get_top_headlines(top_headlines_articles)
    sources_list = get_top_sources(sources_articles, headlines)
    context = {
        'sources_articles': sources_list,
        'top_headlines': top_headlines_articles
    }

    return render(request, 'sources.html', context)


@login_required(login_url='/accounts/login/')
def articles(request):

    global newsapi
    top_headlines = newsapi.get_top_headlines(
        country='us',
        language='en',
    )

    top_headlines_articles = top_headlines['articles']
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
            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            HttpResponseRedirect('news_today')

    return render(request, 'email/newsletter,html', {"date": date, "news": news, "form": form})
