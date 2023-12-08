from django.contrib import admin

from core.models import Creator, Poll


@admin.register(Creator)
class Creator(admin.ModelAdmin):
    list_display = ['nick']


@admin.register(Poll)
class Poll(admin.ModelAdmin):
    list_display = ['theme']
