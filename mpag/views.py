from django.core.paginator import (
    Paginator, PageNotAnInteger, EmptyPage,
)
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import (
    DetailView,
)
from .models import (
    Room,
    Note,
    Book,
)


def index(request):
    return HttpResponse("Hello, world. You're at the mpag index.")


class MpagDetailView(DetailView):
    template_name = 'mpag/detail.html'
    context_object_name = 'object'
    pk_url_kwarg = 'room_id'
    model = Room
    
    def get_context_data(self, **kwargs):
        # call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # create paginator for notes
        all_notes = Note.objects.all()
        paginator = Paginator(all_notes, 4)
        page = self.request.GET.get('page1')
        try:
            all_notes = paginator.page(page)
        except PageNotAnInteger:
            all_notes = paginator.page(1)
        except EmptyPage:
            all_notes = paginator.page(paginator.num_pages)
        # create paginator for books
        all_books = Book.objects.all()
        paginator = Paginator(all_books, 3)
        page = self.request.GET.get('page2')
        try:
            all_books = paginator.page(page)
        except PageNotAnInteger:
            all_books = paginator.page(1)
        except EmptyPage:
            all_books = paginator.page(paginator.num_pages)
        # add all Notes & Books to context
        context['notes'] = all_notes
        context['books'] = all_books
        return context

    # todo:test:added for testing
    def get_object(self, queryset=None):
        object = super().get_object(queryset=queryset)
        return object

