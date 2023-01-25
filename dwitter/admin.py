from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Dweet


class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    # mostrar somente o campo username
    fields = ["username"]
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# revmove a visualização dos grupos
admin.site.unregister(Group)
# admin.site.register(Profile)
admin.site.register(Dweet)
