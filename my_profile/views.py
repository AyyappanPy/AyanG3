from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/')
def profile(request):
    return render(request, 'my_profile/profile_menus.html', {})