from django.shortcuts import render
from .models import Tweet

# Create your views here.

def index(request):
	contex={"value":"VALOR CONTEX","model":Tweet.objects.get(id=1)}
	return render(request,"tweets/index.html",contex)