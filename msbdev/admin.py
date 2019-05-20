from django.contrib import admin

# Register your models here.
from msbdev.models import TextCopy, ContactForm


class ContactFormAdmin(admin.ModelAdmin):
    list_display = [
        'email',
        'note'
    ]

    search_fields = list_display


admin.site.register(TextCopy)
admin.site.register(ContactForm, ContactFormAdmin)
