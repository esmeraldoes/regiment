

from rest_framework import generics, status, permissions
from rest_framework.response import Response

from .models import Church, Community, Team
from .serializers import ChurchSerializer, CommunitySerializer, TeamSerializer, UserSerializer

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter

from rest_framework.decorators import api_view
from rest_framework.response import Response
from grpc import insecure_channel
import prayer_tracker_pb2
import prayer_tracker_pb2_grpc



from rest_framework.views import APIView
from rest_framework.response import Response
from prayer_tracker_pb2 import StartPrayerRequest, PrayerRequest, EndPrayerRequest
from prayer_tracker_pb2_grpc import PrayerTrackerServiceStub
import grpc

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from rest_auth.registration.views import SocialLoginView
from .serializers import CustomLoginSerializer
from rest_framework.authentication import TokenAuthentication

class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    


class LoginView(ObtainAuthToken):
    serializer_class = CustomLoginSerializer  # Set the serializer class
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


from rest_framework import serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class CustomLogoutSerializer(serializers.Serializer):
    def logout(self):
        request = self.context.get('request')
        if request.auth:
            Token.objects.filter(key=request.auth.key).delete()


class LogoutView(ObtainAuthToken):
    serializer_class = CustomLogoutSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.logout()
        return Response(status=status.HTTP_200_OK)



class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class ChurchCreateView(generics.CreateAPIView):
    queryset = Church.objects.all()
    serializer_class = ChurchSerializer
    permission_classes = [AllowAny]
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommunityCreateView(generics.CreateAPIView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TeamCreateView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StartPrayerView(APIView):
    def post(self, request):
        user_id = request.POST.get('user_id')

        # user_id = request.data['user_id']
        # user_id = request.data.get('user_id')

        channel = grpc.insecure_channel('localhost:80001')
        stub = PrayerTrackerServiceStub(channel)
        response = stub.StartPrayer(StartPrayerRequest(user_id=user_id))
        return Response({'message': response.message})

class EndPrayerView(APIView):
    def post(self, request):
        user_id = request.POST.get('user_id')
        # user_id = request.data['user_id']
        channel = grpc.insecure_channel('localhost:80001')
        stub = PrayerTrackerServiceStub(channel)
        response = stub.EndPrayer(EndPrayerRequest(user_id=user_id))
        return Response({'message': response.message})

class PrayerUpdatesView(APIView):
    def post(self, request):
        user_id = request.POST.get('user_id')
        # user_id = request.data['user_id']
        channel = grpc.insecure_channel('localhost:80001')
        stub = PrayerTrackerServiceStub(channel)
        prayer_request = PrayerRequest(user_id=user_id)
        prayer_updates = stub.PrayerUpdates(prayer_request)
        return Response(prayer_updates)
