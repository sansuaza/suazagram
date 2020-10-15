from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, FormView, UpdateView
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
# Create your views here.

 

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile
# Users
from users.forms import  SignupForm


class UserDetailView(LoginRequiredMixin, DetailView):

    template_name = 'users/detail.html'

     #Slug campo de texto unico
    slug_field = 'username'

        
    slug_url_kwarg = 'username'

    #Se definen los conjuntos de datos que se quieren detallar
    queryset = User.objects.all()

    #Contexto en el que se va mover el detalle para agregar sus posts
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """ agrega los posts del usuario """

        #usa los datos que hubiera utilizado si no se hubiera sobreescrito el metodo
        context = super().get_context_data( **kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user= user).order_by('-created')
        return context
    

class SignupView(FormView):

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

"""
    def signup_view(request):
    if request.method == 'POST':
        form = signupForm(request.POST) 

        if form.is_valid():
            form.save()

            return redirect('users:login')

    else:
        form = SignupForm()

    return render(
        request= request,
        template_name= 'users/signup.html',
        context={'form': form}
    )
 """

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    
    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    def get_object(self):
        """obtiene el objeto que está en la sesion"""
        return self.request.user.profile

    def get_success_url(self):
        username= self.object.user.username
        return reverse('users:detail', kwargs={'username':  username})

"""
@login_required
def update_profile(request):

    profile = request.user.profile

    if request.method == 'POST':
     
        #Las imagenes no son solo texto de formularios, Por eso el request.FILES
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
          
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            #
            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)
            
    else:
        form = ProfileForm()

    # el form se tiene que agregar para  poder tenerlo disponible en el template
    return render(
        request = request,
        template_name = 'users/update_profile.html',
        context = {
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )
"""

class LoginView(auth_views.LoginView):
    template_name  = 'users/login.html'
    redirect_authenticated_user = True
"""
def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username,password=password)

        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render (request, 'users/login.html', 
            {'error': 'invalid username and password'})

    return render(request, 'users/login.html')
"""

class LogOutView(LoginRequiredMixin, auth_views.LogoutView):
    template_name = 'users/logged_out.html'


"""
@login_required
def logout_view(request):
    logout(request) 
    return redirect('users:login')
"""
 

