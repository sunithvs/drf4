"""
registration.admin
"""

from django.contrib import admin
from .models import Registration

import csv
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.utils.timezone import now


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'session', "verified"]

    actions = ['export_as_csv', 'verify_registration']

    def verify_registration(self, request, queryset):
        message_bit = "1 registration was"
        if queryset.count() > 1:
            message_bit = "%s registrations were" % queryset.count()
        self.message_user(request, "%s successfully verified." % message_bit)

        for obj in queryset:
            obj.verified = True
            obj.save()
        queryset.update(verified=True)

    verify_registration.short_description = 'Verify selected registrations'

    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=registrations-%s.csv' % now().strftime('%Y-%m-%d')
        writer = csv.writer(response, csv.excel)
        response.write(u'\ufeff'.encode('utf8'))
        writer.writerow([
            smart_str(u"Name"),
            smart_str(u"Email"),
            smart_str(u"Phone"),
            smart_str(u"College"),
            smart_str(u"Session"),
            smart_str(u"Coupon"),
            smart_str(u"Verified"),
        ])
        for obj in queryset:
            writer.writerow([
                smart_str(obj.name),
                smart_str(obj.email),
                smart_str(obj.phone),
                smart_str(obj.college),
                smart_str(obj.session),
                smart_str(obj.coupon),
                smart_str(obj.verified),
            ])
        return response


admin.site.register(Registration, RegistrationAdmin)
