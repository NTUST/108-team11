from django.contrib import admin
from mysite.models import user
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ['name', 'role', 'family', 'education', 'friendship', 'health', 'wealth', 'love']
		

admin.site.register(user, UserAdmin)