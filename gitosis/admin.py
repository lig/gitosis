from django.contrib import admin

from models import GitosisRepo, GitosisUser, GitosisGroup


admin.site.register((GitosisRepo, GitosisUser, GitosisGroup,))
