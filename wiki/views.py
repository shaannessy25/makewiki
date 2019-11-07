from django.shortcuts import render
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PageList(ListView):
    """
      This class will show the user an overview of the page content and render all of the wiki pages
    """
    model = Page

    def get(self, request):
        """ Returns a list of all pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {'pages': pages})


class PageDetailView(DetailView):
    """
      Renders a specific page based on it's slug
    """
    model = Page

    def get(self, request, slug):
        """ Returns a specific of wiki page by slug. """
        page = self.getqueryset().get(slug_iexact=slug)
      
        return render(request, 'page.html', {'page': page})

    def post(self, request, slug):
        pass
