from django import forms
from .models import Login
from .models import Register
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('username', 'password')




class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('register_username', 'register_password', 'register_repeat_password')

    def clean_register_username(self):
        username = self.cleaned_data['register_username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(u'Username "%s" is already in use.' % username)
        return username

    def clean(self):
        if 'password' in self.cleaned_data and 'repeat_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['repeat_password']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data