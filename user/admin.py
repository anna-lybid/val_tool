from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User

admin.site.regiser(User, UserAdmin)
