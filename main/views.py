from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import Article
from main.forms import ArticleForm
from markdownx.utils import markdownify
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
import json

def home(request):
    articles = Article.objects.all().order_by('-created')
    context = {
        'articles': articles
    }

    return render(request, template_name='main/home.html', context=context)

def article_detail(request, pk):
    article = Article.objects.get(pk=pk)
    article.body = markdownify(article.body)
    context = {
        'article': article
    }

    return render(request, template_name='main/article.html', context=context)

@login_required()
def article_new(request):
    if request.method == 'GET':
        form = ArticleForm(initial={
            # 'author':get_user_model().objects.get(username='admin')
            'author':get_user_model().objects.get(pk=request.user.id)
        })

    elif request.method == 'POST':
        form = ArticleForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('main:home')

    context = {
        'form': form,
        'current': 'new',
    }

    return render(request, template_name='main/article_form.html', context=context)

@login_required()
def article_delete(request, pk):
    if request.method == 'DELETE':
        try:
            article = Article.objects.get(id=pk)

            if request.user.id != article.author.id:
                return HttpResponse("잘못된 접근입니다.")

            article.delete()
            response = {
                'status': 1,
                'next_url': str(reverse_lazy('main:home')),
            }
        except:
            response = {
                'status': -1,
            }

        return HttpResponse(json.dumps(response), content_type='application/json')



def article_edit(request, pk):
    article = Article.objects.get(id=pk)

    if request.user.id != article.author.id:
        return HttpResponse("잘못된 접근입니다.")

    if request.method == 'GET':
        form = ArticleForm(initial={
            'author':request.user.id,
            'title':article.title,
            'body':article.body
        })

    elif request.method == 'POST':

        if article.title != request.POST['title']:
            article.title = request.POST['title']

        if article.body != request.POST['body']:
            article.body = request.POST['body']

        article.save()

        return redirect('main:article_detail', article.id)

    context = {
        'form': form,
        'current': 'edit',
        'article': pk
    }

    return render(request, template_name='main/article_form.html', context=context)
