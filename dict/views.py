from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from itertools import chain
from operator import attrgetter

from .models import Word, WordTL

def index(request):
    word_list = Word.objects.order_by('word')
    context = {'word_list': word_list}
    
    ifsearch = site_search(request)
    if ifsearch:
        return ifsearch
    else:
        paginator = Paginator(word_list,  100)  
        page = request.GET.get('page')
        try:
            word_list_paged = paginator.page(page)
        except PageNotAnInteger:
            word_list_paged = paginator.page(1)
        except EmptyPage:
            word_list_paged = paginator.page(paginator.num_pages)                
        context = {'word_list': word_list_paged}
        return render(request, 'dict/index.html', context)

def detail(request, word):
    word_list = get_list_or_404(Word, word=word)
    context = {'word_list': word_list, 'term':word}
    
    ifsearch = site_search(request)
    if ifsearch:
        return ifsearch
    else:
    
        return render(request, 'dict/detail.html', context)
        
def about(request):
    ifsearch = site_search(request)
    if ifsearch:
        return ifsearch
    else:   
        return render(request, 'dict/about.html')

def search(request, word):
    word = word.replace('(.*<qm>)', '(.*?)') #additional regex replacements
    #should probably stay that way due to how japanese works
    
    #html title recreation
    searchword = word.replace('(.)', '?').replace('(.*?)', '*')
    
    by_word_list = Word.objects.filter(word__iregex=r'{0}'.format(word))    
    by_reading_list = Word.objects.filter(reading__iregex=r'{0}'.format(word))    
    
    meaning_list = WordTL.objects.filter(translation__iregex=r'\b{0}\b'.format(word))    
    by_meaning_list = Word.objects.filter(id__in=meaning_list.values('word')).order_by('word')
    
    #whatever, it's fine atm / with kanji update maybe
    #still need to include better detection of how common word is, update db import
    #word_list = sorted(chain(by_word_list, by_reading_list, by_meaning_list), key=attrgetter('common', 'word'), reverse=True)

    word_list = by_word_list | by_reading_list | by_meaning_list
    word_list = sorted(word_list, key=lambda x: (-x.common, len(x.word), x.word))
    
    paginator = Paginator(word_list, 25)  #25 per page

    #paginator
    page = request.GET.get('page')
    try:
        word_list_paged = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        word_list_paged = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        word_list_paged = paginator.page(paginator.num_pages)        
        
    context = {'word_list': word_list_paged, 'searchterm':searchword}
    
    ifsearch = site_search(request)
    if ifsearch:
        return ifsearch
    else:
        return render(request, 'dict/search.html', context)
    
    #for generic search, useable anywhere
def site_search(request):
    query = request.GET.get('search')
    if query:
        #works with ? and *
        query = query.replace('?', '(.)').replace('*','(.*<qm>)')
        return HttpResponseRedirect('/s/%s/' %query)
    else:
        return
        