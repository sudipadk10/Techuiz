from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)