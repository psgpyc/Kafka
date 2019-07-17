from django.shortcuts import render,get_object_or_404, redirect
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views import View

from .models import Post,Comments

from django.contrib.auth.mixins import UserPassesTestMixin

from django.contrib.auth.models import User

from .forms import CommentForm

from django.core.paginator import Paginator

from django.contrib import messages

class Home(View):
    template_name = 'blog/home.html'

    def get(self, request , *args , **kwargs):
        post = Post.objects.all()
        cmt = Comments.objects.all()
        c_form = CommentForm()
        paginate_by = Paginator(post,3)
        page = request.GET.get('page')
        post = paginate_by.get_page(page)

        ctx = {
            'title': 'Home',
            'posts': post,
            'c_form' : c_form,
            'comment' : cmt,

        }
        return render(request, template_name=self.template_name,context=ctx)

    def post(self, request , *args , **kwargs):
        form = CommentForm(request.POST)
        post_of = Post.objects.get(title=request.POST['ipost'])


        if form.is_valid():
            comm=form.save()
            print(form.cleaned_data)
            comm.comment_by = request.user
            comm.post = post_of
            comm.save()
            return redirect('blog-home')



class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserPostListView,self).get_context_data(**kwargs)
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        context['usr'] = user
        context['title'] = 'test'
        return context



class PostDetailView(DetailView):
    model = Post


    def get_context_data(self, **kwargs):

        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['title'] = 'Post'
        return context

class PostCreateView(CreateView):
    model = Post


    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):

        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Post'
        return context




class PostUpdateView(UserPassesTestMixin,UpdateView):
    model = Post

    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class About(View):
    template_name = 'blog/about.html'

    def get(self, request, *args, **kwargs):
        return render(request , template_name=self.template_name, context={'title': 'Books'})




