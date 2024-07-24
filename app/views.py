from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length


def insert_topic(request):
    tn=input("enter topic_name")
    T=Topic.objects.get_or_create(topic_name=tn)[0]
    T.save()
    return HttpResponse("Topic is created")



def insert_WebPage(request):
    wn=input("enter topic_name")
    name=input("enter name")
    url=input("enter url")
    email=input("enter email")
    T=Topic.objects.get(topic_name=wn)
    T.save()
    w=WebPage.objects.create(topic_name=T,name=name,url=url,email=email)
    return HttpResponse("WebPage is created")


def insert_AccessRecord(request):
    name=input("enter name")
    author=input("enter author")
    date=input("enter date")
    W=WebPage.objects.get_or_create(name=name)[0]
    i=AccessRecord.objects.create(name=W,author=author,date=date)
    return HttpResponse("AccessRecord is created")



def retrieve_topics(request):
    t=Topic.objects.all()
    t=Topic.objects.values('topic_name')
    t=Topic.objects.exclude(topic_name='volleyball')
    t=Topic.objects.all()[2::]
    t=Topic.objects.order_by('topic_name')
    t=Topic.objects.order_by('-topic_name')
    t=Topic.objects.order_by(Length('topic_name'))
    t=Topic.objects.order_by(Length('topic_name').desc())
    t=Topic.objects.filter(topic_name__endswith ="l")
    t=Topic.objects.filter(topic_name__in=['cricket','volleyball','football',])
    t=Topic.objects.filter(topic_name__contains='v')
    d={'topics':t}
    return render(request,'retrieve_topics.html',d)


def retrieve_webpages(request):
    w=WebPage.objects.all()
    w=WebPage.objects.values('name')
    w=WebPage.objects.exclude(topic_name="cricket")
    w=WebPage.objects.all()[::-2]
    w=WebPage.objects.order_by('name')
    w=WebPage.objects.order_by('-topic_name')
    w=WebPage.objects.order_by(Length('name'))
    w=WebPage.objects.order_by(Length('topic_name').desc())
    w=WebPage.objects.filter(name__endswith ="h")
    w=WebPage.objects.filter(name__startswith='v')
    w=WebPage.objects.filter(topic_name__in=['cricket','volleyball'])
    w=WebPage.objects.filter(name__in=['virat','vansh','kedar'])
    w=WebPage.objects.filter(url__in=['https://virat.com','https://vansh.com','https://yash.com'])
    w=WebPage.objects.filter(name__contains='y')
    d={'webpages':w}
    return render(request,'retrieve_webpages.html',d)


def retrieve_access(request):
    a=AccessRecord.objects.all()
    a=AccessRecord.objects.values('author')
    a=AccessRecord.objects.exclude(name=3)
    a=AccessRecord.objects.all()[1::]
    a=AccessRecord.objects.order_by('author')
    a=AccessRecord.objects.order_by('-name')
    a=AccessRecord.objects.order_by(Length('author'))
    a=AccessRecord.objects.order_by(Length('author').desc())
    a=AccessRecord.objects.filter(author__endswith="a")
    a=AccessRecord.objects.filter(id__startswith=1)
    a=AccessRecord.objects.filter(name__in=[4])
    a=AccessRecord.objects.filter(date__gte='2002-05-30')
    a=AccessRecord.objects.filter(date__lte='2025-05-30')
    a=AccessRecord.objects.filter(author__contains='h')
    d={'access':a}
    return render(request,'retrieve_access.html',d)
    

