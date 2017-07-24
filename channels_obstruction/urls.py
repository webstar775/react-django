"""channels_obstruction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from game.views import *
from django.contrib.auth.views import login, logout
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', CreateUserView.as_view()),
    url(r'^login/$', login, {'template_name': 'login.html'}),
    url(r'^logout/$', logout, {'next_page': '/'}),
    url(r'^lobby/$', LobbyView.as_view()),

    url(r'^$', HomeView.as_view())
]

# urls for api - django rest framework
urlpatterns += [
 url(r'^current-user/', CurrentUserView.as_view()),
]
router = DefaultRouter()
router.register(r'player-games', PlayerGameViewSet, 'player_games')
urlpatterns += router.urls
