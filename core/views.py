from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from core import models, forms, filters


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


class BookList(TitleMixin, ListView):
    model = models.Book
    template_name = 'bookpage.html'
    context_object_name = 'book'
    title = 'Книги'

    def get_filters(self):
        return filters.BookFilter(self.request.GET)

    def get_queryset(self):
        # title = self.request.GET.get('title')
        # num_of_reviews = self.request.GET.get('num_of_reviews')
        # qs = models.Book.objects.all()
        # if title or num_of_reviews:
        #     return qs.filter(Q(title__icontains=title) | Q(num_of_reviews=num_of_reviews))
        return self.get_filters().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.get_filters()
        context['count'] = self.get_queryset().count()
        return context


class AuthorDetail(TitleMixin, DetailView):
    model = models.Author
    template_name = 'authordetail.html'
    context_object_name = 'author'
    title = "Автор"


class BookCreate(TitleMixin, CreateView):
    model = models.Book
    template_name = 'book_create.html'
    context_object_name = 'book_create'
    form_class = forms.BookForm
    success_url = reverse_lazy('core:book_list')
    title = "Добавление книги"


class BookUpdate(TitleMixin, UpdateView):
    model = models.Book
    template_name = 'book_update.html'
    context_object_name = 'book_update'
    form_class = forms.BookForm
    success_url = reverse_lazy('core:book_list')
    title = "Редактирование книги"


class BookDelete(TitleMixin, DeleteView):
    model = models.Book
    template_name = 'book_delete.html'
    context_object_name = 'book_delete'
    success_url = reverse_lazy('core:book_list')
    title = "Удаление книги"

# def get_book_list(request):
#    name = request.GET.get('title')
#    if name:
#        book = models.Book.objects.filter(title__icontains=name)
#    else:
#        book = models.Book.objects.all()
#    book_count = book.count()
#    context = {'book': book, 'count': book_count}
#    return render(request=request, template_name='bookpage.html', context=context)

# def get_author(request, pk):
#    author = get_object_or_404(models.Author, pk=pk)
#    context = {'author': author}
#    return render(request=request, template_name='author.html', context=context)
