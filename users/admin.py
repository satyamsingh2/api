
from django.contrib import admin
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display=[
        'id',
        'first_name',
        'last_name',
    ]
    search_fields=('id', 'first_name', 'last_name')
    list_filter= ('id', 'first_name', 'last_name')

admin.site.register(Member, MemberAdmin)
