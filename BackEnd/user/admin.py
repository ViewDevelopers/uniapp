from django.contrib import admin
from user.models import User, UserType, IDType, AdminAccount

admin.site.register(User)
admin.site.register(UserType)
admin.site.register(IDType)
admin.site.register(AdminAccount)