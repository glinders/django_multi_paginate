from django.core.paginator import (
    Paginator, Page, PageNotAnInteger, EmptyPage,
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


class MyPaginator(Paginator):
    # override _get_page to insert our version of class Page
    # I've copied the original docstring of _get_page as a reference
    # that this is the intended way to do this
    def _get_page(self, *args, **kwargs):
        """
        Return an instance of a single page.

        This hook can be used by subclasses to use an alternative to the
        standard :cls:`Page` object.
        """
        return MyPage(*args, **kwargs)


class MyPage(Page):
    def current_page_number(self):
        return self.paginator.validate_number(self.number)


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
        paginator = MyPaginator(all_notes, 4)
        page = self.request.GET.get('page1')
        try:
            all_notes = paginator.page(page)
        except PageNotAnInteger:
            all_notes = paginator.page(1)
        except EmptyPage:
            all_notes = paginator.page(paginator.num_pages)
        # create paginator for books
        all_books = Book.objects.all()
        paginator = MyPaginator(all_books, 3)
        page = self.request.GET.get('page2')
        try:
            all_books = paginator.page(page)
        except PageNotAnInteger:
            all_books = paginator.page(1)
        except EmptyPage:
            all_books = paginator.page(paginator.num_pages)
        # add paginated Notes & Books to context
        context['notes'] = all_notes
        context['books'] = all_books
        return context

    # todo:test:added for testing
    def get_object(self, queryset=None):
        object = super().get_object(queryset=queryset)
        return object

