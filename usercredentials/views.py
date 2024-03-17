from django.shortcuts import render
from django.views.generic.edit import CreateView
from . import models
from . forms import ProfileCreationForm
from django.urls import reverse_lazy
from django.contrib import auth
from django.forms.models import model_to_dict

# Create your views here.

def dashboard(request):
    context = {}
    if request.user.is_authenticated:
        userobj = models.Profile.objects.get(id = request.user.id)
        userobj = model_to_dict(userobj)
        fields = ['username', 'email', 'firstName', 'lastName', 'address', 'profilePicture', 'password']
        context = {'fields':fields, 'userobj':userobj.items()}
    return render(request, 'dashboard.html', context)

def signupNavigator(request):
    return render(request, 'signup_nav.html')


class ProfileCreateView(CreateView):
    model = models.Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('dashboard')


class DoctorSignUp(ProfileCreateView):
    template_name = 'doctorSignup.html'

    def onsucces(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = auth.authenticate(username = username, password = password)
        obj = models.Profile.objects.get(username=username)
        obj.role = True
        obj.save()
        auth.login(self.request, user)
        return user

    def form_valid(self, form):
        response = super().form_valid(form)
        self.onsucces(form)
        return response

class UserSignUp(ProfileCreateView):
    template_name = 'userSignup.html'
    
    def onsucces(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = auth.authenticate(username = username, password = password)
        auth.login(self.request, user)
        obj = models.Profile.objects.get(username=username)
        obj.role = False
        obj.save()
        return user

    def form_valid(self, form):
        response = super().form_valid(form)
        self.onsucces(form)
        return response
    

    



