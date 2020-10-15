
#Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletationMiddleware:
    """
    Asegura  que el usuario tenga foto de perfil y 
    biografia para poder interactuar con la plataforma
    """

    def __init__(self, get_response):
        #Middleware initialization
        self.get_response = get_response


    def __call__(self, request):
        #Code to be executed for each request
        
        """
        Gracias a los middleware se pueden pedir estos
        datos en cualquier template, en la condicion se pide
        que si hay un usuario loggueado

        """
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile

                if not profile.picture or not profile.biography:
                    if request.path not in  [reverse('users:update') 
                    , reverse('users:logout')]:
                        return redirect('users:update')
            

        response = self.get_response(request)
        return response