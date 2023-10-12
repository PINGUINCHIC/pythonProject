from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Post, Author
from datetime import datetime
from django.utils import timezone
from django.shortcuts import render
from django.views import View
from django.db.models import QuerySet
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm

class PostList(ListView):
    model = Post
    template_name = 'newapp/news.html'
    context_object_name = 'news'

    paginate_by = 10

    def get_queryset(self) -> QuerySet(any):
        post_filter = PostFilter(self.request.GET, queryset=Post.objects.all())
        return post_filter.qs.order_by('-dateCreation')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = timezone.localtime(timezone.now())
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return super().get(request, *args, **kwargs)

class PostDetail(DetailView):
    model = Post
    template_name = 'newapp/new_detail.html'
    context_object_name = 'news'
    queryset = Post.objects.all()

class News(View):

    def get(self, request):
        news = Post.objects.order_by('-dateCreation')
        p = Paginator(news, 1)
        news = p.get_page(
            request.GET.get('page', 1))


        data = {
            'news': news,
        }

        return render(request, 'newapp/search.html', data)

class PostCreateView(CreateView):
    template_name = 'newapp/new_create.html'
    form_class = PostForm
    context_object_name = 'news'

    def form_valid(self, form):
        author_name = form.cleaned_data['author']

        author, created = Author.objects.get_or_create(name=author_name)

        form.instance.author = author

        return super().form_valid(form)


class PostUpdateView(UpdateView):
    template_name = 'newapp/new_create.html'
    form_class = PostForm
    context_object_name = 'news'


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'newapp/new_delete.html'
    queryset = Post.objects.all()
    success_url = reverse_lazy('newapp:news')
    context_object_name = 'news'



