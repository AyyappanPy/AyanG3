from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponse, HttpResponsePermanentRedirect
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
                    print
                    auth_login(request, user)
                    return HttpResponsePermanentRedirect(reverse('my_profile:profile'))
                else:
                    return render(request, 'login/page_not_found.html', {})
            else:
                return render(request, 'login/page_not_found.html', {})
        else:
            if request.POST.get('type') == 'register':
                form = RegisterForm(request.POST)
                if form.is_valid():
                    user = User.objects.create_user(
                        username=form.cleaned_data['register_username'],
                        password=form.cleaned_data['register_password'],
                    )
                    return HttpResponsePermanentRedirect(reverse('my_profile:profile'))
                else:
                    return render(request, 'login/page_not_found.html', {})
    else:
        if request.user.is_authenticated():
            return HttpResponsePermanentRedirect(reverse('my_profile:profile'))
        else:
            return render(request, 'login/login_forms.html', {})

def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)

def signout(request):
    print "^^^^^^^^^^^^^^^^^^^^^^^^^^"
    if request.user.is_authenticated():
        print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
        logout(request)
        return render(request, 'login/login_forms.html', {})
