from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed, ValidationError, NotFound
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import CustomUser
from ..serializers.user import UserSerializer
from rest_framework.response import Response


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=False)
    def login(self, request):
        if 'email' not in request.data:
            data = {'email': ['Email должен быть заполнен']}
            if 'password' not in request.data:
                data['password'] = ['Пароль должен быть заполнен']
            raise ValidationError(data)
        if 'password' not in request.data:
            raise ValidationError(
                {'password': ['Пароль должен быть заполнен']})

        try:
            user = CustomUser.objects.get(email=request.data.get('email'))
        except CustomUser.DoesNotExist:
            raise NotFound(
                {'message': 'User with provided credentials does not exist'})

        if not user.check_password(request.data.get('password')):
            raise AuthenticationFailed({'message': 'Incorrect password'})

        refresh = RefreshToken.for_user(user)
        response = Response()
        response.set_cookie('refresh', str(refresh))
        response.data = {'access': str(refresh.access_token)}
        return response
