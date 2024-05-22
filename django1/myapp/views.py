from django.shortcuts import render, HttpResponse, redirect
from .models import Article
from .forms import CreateArticle
from . import forms
# Create your views here.
def index(request):
    articles = Article.objects.all()

    return render(request, "index.html", {"articles": articles})


def get_article(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, "article.html", {"article": article})



def create_article(request):
    if request.method == 'POST':
        form = CreateArticle(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:index')
    else:
        form = forms.CreateArticle()
    return render(request, "create-article.html", {"form": form})