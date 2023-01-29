from django.contrib import admin
from user.models import User, UserType, IDType, AdminAccount

class AdminAccountAdmin(admin.ModelAdmin):
    list_display = ('admin_name', 'email', 'is_staff', 'is_superuser', 'is_active')
    list_display_links = ('admin_name', 'email')
    search_fields = ('admin_name', 'email', 'is_staff', 'is_superuser', 'is_active')
    list_per_page = 20

admin.site.register(User)
admin.site.register(UserType)
admin.site.register(IDType)
admin.site.register(AdminAccount, AdminAccountAdmin)