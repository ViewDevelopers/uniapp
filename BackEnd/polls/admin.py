from django.contrib import admin

from polls.models import Period, Candidate, Position, Poll

admin.site.register(Period)
admin.site.register(Candidate)
admin.site.register(Position)
admin.site.register(Poll)
