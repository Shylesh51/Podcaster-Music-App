from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class PodcastLoginView(LoginView):
    template_name="account/login.html"

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return redirect('home')
        
        else:
            return self.form_invalid(form)
        
def logout_view(request):
    logout(request)
    return redirect('home')


class RegisterView(View):
    template_name = "account/register.html"

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, context={'form': form})
    
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        
        return render(request, self.template_name, {'form': form})