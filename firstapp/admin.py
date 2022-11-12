from django.contrib import admin
from .models import Person,Msg

# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    pass

class MsgAdmin(admin.ModelAdmin):
    pass

admin.site.register(Msg, MsgAdmin)

admin.site.register(Person, PersonAdmin)

