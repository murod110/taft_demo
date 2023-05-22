from django.contrib import admin
from .models import BotUser, Feedback, Palet, Charakter
# Register your models here.
admin.site.register(BotUser)
admin.site.register(Feedback)
admin.site.register(Palet)
admin.site.register(Charakter)