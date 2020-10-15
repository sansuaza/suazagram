from django import forms

#Models
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm (forms.Form):

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50
    )

    email = forms.CharField(
        min_length=6, 
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        #trae los datos ya limpios por parte de django con ese usuario
        username = self.cleaned_data['username']

        #filtra por el username ingresado,y si hay alguno queda con valor true
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username


    def clean(self):
        """verify password and password_conf match"""

        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('password do not match.')

        return data
        
    def save(self):
        data = self.cleaned_data

        #Se elimina este dato de la data ya que no es necesario
        data.pop('password_confirmation')

        #Manda  todo el diccionario con los dos asteriscos
        user= User.objects.create_user(**data)
        profile= Profile(user = user)
        profile.save()



"""
class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=12, required=False)
    picture = forms.ImageField()
"""