from datetime import datetime

from django.conf.urls.defaults import *
from django.contrib import admin

from csesoc import settings
from csesoc.campattendees.views import signup
from csesoc.campleaders.views import apply
from csesoc.game.views import game_scores, game_static, game_static_latest
from csesoc.mainsite.views import static, thedate
from csesoc.scheduler.views import join, results
from csesoc.sponsors.views import sponsors
from csesoc.music.views import music_submit_song, music_vote

admin.autodiscover()


urlpatterns = patterns('',

    # admin site
    (r'^admin/(.*)', 'csesoc.auth.backends.admin_wrapper'),

    # statics path
    (r'static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_URL}),

    # login redirect
    (r'accounts/login/$', 'csesoc.auth.backends.cse_login'),

    # camp leader applications
    (r'^apply/$', apply),
    # camp attendee applications
    (r'^signup/$', signup),

    # suggestions form
    (r'^suggestions/', include('csesoc.suggestions.urls')),

    # scheduler signup
    (r'^oweek/signup/$', join),
    (r'^oweek/slots/$', results),

    # sponsors page
    (r'^sponsors/$', sponsors),

    # urls for murder
    (r'^murder/', include('csesoc.murder.urls')),

    # url for the game
    (r'^game/scores/(?P<year>[0-9]*)$', game_scores),
    (r'^game/scores$', game_scores, {'year':''}),
    (r'^game/$', game_static_latest),
    (r'^game/(?P<path>.*)$', game_static),

    # urls for music
    (r'^music/$', music_submit_song),
    (r'^music/vote/$', music_vote),

    # news-related stuff
    (r'^', include('csesoc.mainsite.urls')),

    # the date
    (r'^thedate/$', thedate),

    # miscellaneous articles
    (r'^(?P<path>.*)/$', static),
)

