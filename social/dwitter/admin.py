from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile
#admin.site.register(Profile)
#admin.site.unregister(Group)


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display the "username" field
    fields = ["username"]
    inlines = [ProfileInline]

# Register your models here.


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)