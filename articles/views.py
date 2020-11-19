from django.shortcuts import render
from . import models

# Create your views here.
def articles_list(request):
    articles = models.article.objects.all().order_by('date') #ba order by moratab sazi mishe
    args =  {'articles' : articles}
    return render(request , 'articles/articles_list.html' , args)
