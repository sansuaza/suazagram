
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, CreateView, ListView
#models
from posts.models import Post

#Forms
from posts.forms import PostForm

#Utilities

# Create your views here.

class PostsDetailView(LoginRequiredMixin, DetailView):
    template_name = 'posts/detail.html'
    slug_field= 'id'
    slug_url_kwarg ='id'

    queryset = Post.objects.all()

    context_object_name = 'post'


"""List of all the posts"""
class PostsFeedView(LoginRequiredMixin, ListView):
    template_name= 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 15
    context_object_name= 'posts'
    """
#Si no hay una persona logueada, no es posible accder al feed
@login_required
def list_posts(request):

    #Se pone el menos para invertir el orden en el que se crearon
    posts = Post.objects.all().order_by('-created')
    return render (request, 'posts/feed.html', {'posts': posts})
"""

class CreatePostView(LoginRequiredMixin, CreateView):
    template_name= 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

"""
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) 

        if form.is_valid():
            form.save()
            return redirect('posts:feed')

    else:
        form = PostForm()

    return render(
        request= request, 
        template_name= 'posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        })
        """




