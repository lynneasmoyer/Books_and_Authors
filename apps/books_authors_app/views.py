from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books_authors_app/index.html', context)

def add_book(request):
    if request.method == 'POST':
        Book.objects.create(title= request.POST['title'], desc= request.POST['description'])
    return redirect('/')

def show_description(request, book_id):
    context = {
        'book': Book.objects.get(id= book_id),
        'authors': Author.objects.all()
    }
    return render(request, 'books_authors_app/description.html', context)

def authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'books_authors_app/authors.html', context)

def add_author(request):
    if request.method == 'POST':
        Author.objects.create(first_name= request.POST['first_name'], last_name= request.POST['last_name'], notes= request.POST['notes'])
    return redirect('/authors')

def show_notes(request, author_id):
    context = {
        'authors': Author.objects.get(id= author_id),
        'books': Book.objects.all()
    }
    return render(request, 'books_authors_app/notes.html', context)

def add_additional_author(request, book_id):
    if request.method == 'POST':
        book= Book.objects.get(id=book_id)
        author = Author.objects.get(id= request.POST['author'])
        book.authors.add(author)
    return redirect(f'/book/{book_id}/show_description')

def add_additional_book(request, author_id):
    if request.method == 'POST':
        book= Book.objects.get(id= request.POST['book'])
        author = Author.objects.get(id=author_id)
        book.authors.add(author)
    return redirect(f'/author/{author_id}/show_notes')