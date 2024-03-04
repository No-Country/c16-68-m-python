from django.urls import path
from . import views
"""from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)"""
#Leave it in comment for now

urlpatterns = [
    path("list/", views.UserListView.as_view(), name="list-users"),
    path("retrieve/<int:pk>/", views.UserRetrieveView.as_view(), name="retrieve-users"),
    path("create/", views.UserCreateView.as_view(), name="create-users"),
    path("update/<int:pk>/", views.UserUpdateView.as_view(), name="update-users"),
    path("delete/<int:pk>/", views.UserDeleteView.as_view(), name="delete-users"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("test/", views.TestAuthenticationView.as_view(), name="test"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    #path('jwt/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('jwt/token/verify/', TokenVerifyView.as_view(), name='token_verify'),"""
]
