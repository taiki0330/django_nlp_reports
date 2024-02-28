from django.contrib import admin
from .models import GenreModel, CrimeModel, SuspectModel, VictimModel

# Register your models here.
admin.site.register(GenreModel)
admin.site.register(CrimeModel)
admin.site.register(SuspectModel)
admin.site.register(VictimModel)