
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, LoginView, LogoutView
from .views import RegisterView, FacebookLogin, GoogleLogin
from .views import ChurchCreateView, CommunityCreateView, TeamCreateView
from .views import StartPrayerView, EndPrayerView, PrayerUpdatesView

from bibleApp import prayer_tracker_service
urlpatterns = [
    path('accounts/', include('allauth.urls')),
    # ...
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='loginview'),
    path('api/facebook/', FacebookLogin.as_view(), name='facebook_login'),
    path('api/google/', GoogleLogin.as_view(), name='google_login'),
    
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/token/', obtain_auth_token, name='token'),

    path('api/churches/', ChurchCreateView.as_view(), name='church-create'),
    path('api/communities/', CommunityCreateView.as_view(), name='community-create'),
    path('api/teams/', TeamCreateView.as_view(), name='team-create'),
    # ...
    path('start-prayer/', StartPrayerView.as_view(), name='start-prayer'),
    path('end-prayer/', EndPrayerView.as_view(), name='end-prayer'),
    path('prayer-updates/', PrayerUpdatesView.as_view(), name='prayer-updates'),

    path('grpc/prayer_tracker', prayer_tracker_service.serve),

]

