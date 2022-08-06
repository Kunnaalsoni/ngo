from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Student, State, District, Mandal
# Register your models here.
admin.site.register(Student)
admin.site.register(State)
admin.site.register(District)
admin.site.register(Mandal)


class StudentAdmin(ModelAdmin):
    actions = [State]
    list_display = ["state"]
    search_fields = ["state"]