from django import forms
from .models import EditProfile

class EditProfileForm(forms.ModelForm):

    class Meta:
        model = EditProfile
        fields = ('name', 'dob','phoneno', 'address', 'email', 'website')