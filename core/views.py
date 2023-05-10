from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from core import models


class TitleMixin:
    title = None
    def get_title(self):
        return self.title
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_title()
        return context


def home(request):
    return render(request=request, template_name='homepage.html')

# Решил для разнообразия оставить через def.
# Ниже в виде комментария, есть в виде ListView, полностью работоспособна.
# Примечание: только урлы надо тоже убрать из комментов
def get_book_list(request):
    name = request.GET.get('title')
    if name:
        book = models.Book.objects.filter(title__icontains=name)
    else:
        book = models.Book.objects.all()
    book_count = book.count()
    context = {'book': book, 'count': book_count}
    return render(request=request, template_name='bookpage.html', context=context)


# class BookList(TitleMixin, ListView):
#    model = models.Book
#    template_name = 'bookpage.html'
#    context_object_name = 'book'
#    title = 'Книги'

class AuthorDetail(TitleMixin, DetailView):
    model = models.Author
    template_name = 'authordetail.html'
    context_object_name = 'author'
    title = "Автор"

# def get_author(request, pk):
#    author = get_object_or_404(models.Author, pk=pk)
#    context = {'author': author}
#    return render(request=request, template_name='author.html', context=context)
