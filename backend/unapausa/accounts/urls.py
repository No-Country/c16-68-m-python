from django.urls import path
from .views import *
"""from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)"""
#Leave it in comment for now

urlpatterns = [
    path("list/", UserListView.as_view(), name="list-users"),
    path("retrieve/<int:pk>/", UserRetrieveView.as_view(), name="retrieve-users"),
    path("create/", UserCreateView.as_view(), name="create-users"),
    path("update/<int:pk>/", UserUpdateView.as_view(), name="update-users"),
    path("delete/<int:pk>/", UserDeleteView.as_view(), name="delete-users"),
    path("login/", LoginView.as_view(), name="login"),
    path("test/", TestAuthenticationView.as_view(), name="test"),
    path("logout/", LogoutView.as_view(), name="logout"),
    #path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('jwt/token/verify/', TokenVerifyView.as_view(), name='token_verify'),"""
]
