from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.forms import inlineformset_factory
from apps.news.models import News, Images
from apps.news.forms import NewsCreateForm, ImagesForm


class NewsListView(ListView):
    model = News
    template_name = 'index.html'


class NewsDetailView(DetailView):
    model = News
    template_name = 'detail.html'
    pk_url_kwarg = 'pk'


class NewsDeleteView(DeleteView):
    model = News
    pk_url_kwarg = 'pk'
    template_name = 'delete.html'
    success_url = '/'


class NewsCreateView(CreateView):
    model = News
    form_class = NewsCreateForm
    template_name = 'create_post.html'
    success_url = '/'
    extra = 3

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = inlineformset_factory(News, Images, form=ImagesForm, extra=self.extra)(
                self.request.POST, self.request.FILES, instance=self.object
            )
        else:
            data['formset'] = inlineformset_factory(News, Images,form=ImagesForm,extra=self.extra)()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        print(formset)
        if formset.is_valid():
            self.object = formset.save()
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsCreateForm
    template_name = '/'
    success_url = '/'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.save()
        return super().form_valid(form)


