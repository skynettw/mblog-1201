from django.shortcuts import render, redirect
from django.http import HttpResponse
from mainsite.models import Post
import random
from datetime import datetime
from mainsite.models import AccessInfo, Branch, StoreIncome

def homepage(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, "index.html", locals())

def mychart(request, bid=0):
    now = datetime.now()
    if bid==0:
        data = StoreIncome.objects.all()
    else:
        data = StoreIncome.objects.filter(branch=bid)
    return render(request, "mychart.html", locals())

def showpost(request, slug):
	now = datetime.now()
	try:
		post = Post.objects.get(slug=slug)
		return render(request, "post.html", locals())
	except:
		return redirect("/")

def lotto(request):
    lucky = random.randint(1, 42)
    lottos = list()
    for i in range(6):
        lottos.append(random.randint(1, 42))
    
    return render(request, "lotto.html", locals())
    
