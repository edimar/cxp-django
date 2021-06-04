# Register your models here.
from django.contrib import admin
from .models import Cubs
from .models import Cubs_Hist

admin.site.register(Cubs)
admin.site.register(Cubs_Hist)