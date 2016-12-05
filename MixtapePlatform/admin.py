from django.contrib import admin
from django.contrib.auth.models import User
from MixtapePlatform.models import *

# Register your models here.

admin.site.register(Audio)
admin.site.register(Beat)
admin.site.register(Mixtape)
admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Chart)
admin.site.register(Ranking)
admin.site.register(ChartRanking)