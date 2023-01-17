from django.contrib import admin
from registration.models import User, UserType, IDType

admin.site.register(User)
admin.site.register(UserType)
admin.site.register(IDType)