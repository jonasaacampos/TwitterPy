from django.contrib import admin
from django.contrib.auth.models import Group, User



class UserAdmin(admin.ModelAdmin):
    model = User
    # mostrar somente o campo username
    fields = ["username"]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# revmove a visualização dos grupos
admin.site.unregister(Group)

