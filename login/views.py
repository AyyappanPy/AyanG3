from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponsePermanentRedirect
from django.db import IntegrityError
from .forms import LoginForm
from .forms import RegisterForm



# Create your views here.

def login(request):
    if request.method == 'POST':
        if request.POST.get('type') == 'login':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    # return HttpResponsePermanentRedirect(reverse('wine:wine_page'))
                    return render(request, 'login/login_forms.html', {})
        else:
            if request.POST.get('type') == 'register':
                form = RegisterForm(request.POST)
                if form.is_valid():

                    user = User.objects.create_user(
                        username=form.cleaned_data['register_username'],
                        password=form.cleaned_data['register_password'],
                    )
                    # return HttpResponsePermanentRedirect(reverse('wine:wine_page'))

                    return render(request, 'login/login_forms.html', {})
                else:
                    print "++++++++++++++++", form.errors, "++++++++++++++++"
                    return render(request, 'login/register_form.html', {'form':form})
    else:
        return render(request, 'login/login_forms.html', {})