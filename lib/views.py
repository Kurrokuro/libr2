from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import Book, Genre, Author
from django.template import RequestContext
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index( request, page_number = 1):
    book_list = Book.objects.all().order_by('-pub_date')
    genre_list = Genre.objects.all().order_by('name')
    paginator = Paginator(book_list, 8)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    context = {'books': books, 'book_list':book_list, 'genre_list': genre_list}
    return render_to_response('lib/index.html', context, request)


def detail(request, id):
    book = get_object_or_404(Book, pk=id)
    genre_list = Genre.objects.order_by('name')[:15]
    return render(request, 'lib/detail.html', {'book': book, 'genre_list': genre_list})

def vote(request, id):
    book = Book.objects.get(id=id)
    book.vote += 1
    book.save()
    return HttpResponseRedirect(reverse('lib:results', args=(book.id,)))

def unlike(request, id):
    book = Book.objects.get(id=id)
    book.unlike += 1
    book.save()
    return HttpResponseRedirect(reverse('lib:results', args=(book.id,)))

def results(request, id):
    book = get_object_or_404(Book, pk=id)
    genre_list = Genre.objects.order_by('name')[:15]
    return render(request, 'lib/results.html', {'book': book, 'genre_list': genre_list})

def popular(request):
    book_list = Book.objects.all().order_by('-vote')
    genre_list = Genre.objects.all().order_by('name')
    paginator = Paginator(book_list, 8)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    context = {'book_list': book_list, 'books': books, 'genre_list':genre_list}
    return render_to_response('lib/popular_books.html', context, request)

