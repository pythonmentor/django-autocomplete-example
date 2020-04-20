from django.shortcuts import render
from django.http import JsonResponse

from books.models import Book


def complete(request):
    searched_term = request.GET.get("term")
    books = Book.objects.get_all_by_term(searched_term)
    books = [book.title for book in books]
    return JsonResponse(books, safe=False)
