from django.contrib import admin
from .models import Login
from .models import Register

# Register your models here.

# we import (include) the Login model. To make our model visible on the admin page, we need to register the model with admin.site.register(Login)

admin.site.register(Login)
admin.site.register(Register)
