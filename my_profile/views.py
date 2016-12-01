from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request, 'my_profile/profile_menus.html', {})