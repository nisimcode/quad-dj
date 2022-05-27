from django.contrib import admin

from quad_dj_app.models import Word, Profile, Game, Note, Vocab

admin.site.register(Word)
admin.site.register(Vocab)
admin.site.register(Profile)
admin.site.register(Game)
admin.site.register(Note)

