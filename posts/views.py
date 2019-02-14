from django.shortcuts import render
from django.views import generic
from .models import Post
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.contrib.auth import get_user_model
User = get_user_model()


class UserPosts(generic.ListView):
    model = Post
    template_name = "posts/user_posts.html"

    def get_queryset(self):
        try:
            self.post.user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoestNotExist:
            raise Http404
        else:
            return self.author.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.author
        return context

class PostListView(generic.ListView,SelectRelatedMixin):
    model = Post
    fields = '__all__'
    select_related = ('author')

class PostDetailView(generic.DetailView):
    model = Post


class PostCreateView(CreateView, LoginRequiredMixin, SelectRelatedMixin): # TODO: Figure out why login_required decorator isnt working!
    model = Post
    fields = ('title','content')
    template_name = 'posts/post_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


@login_required
class PostUpdateView(UpdateView):
    pass

@login_required
class PostDeleteView(DeleteView):
    pass
