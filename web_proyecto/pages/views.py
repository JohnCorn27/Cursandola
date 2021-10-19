from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Page, Categoria, Video
from .forms import PageForm, PageFormCategoria, PageFormVideo

# Create your views here.
class PageListView(ListView):
    model = Page

class PageDetalView(DetailView):
    model = Page

class PageCreateVideo(CreateView):
    model = Video
    form_class = PageFormVideo
    success_url = reverse_lazy('pages:pages')

class PageCreateCategoria(CreateView):
    model = Categoria
    form_class = PageFormCategoria
    success_url = reverse_lazy('pages:pages')

class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    success_url = reverse_lazy('pages:pages')

class PageUpdate(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'

class PageDelete(DeleteView):
    model = Page
    success_url = reverse_lazy('pages:pages')

