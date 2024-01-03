from django.urls import path, include
from .views import *
from django.contrib.auth.views import logout_then_login


app_name = 'users'

urlpatterns = [
    path("login_rest/", obtain_auth_token, name='login'),
    path("list/", user_list, name='user_list'),
    path("create/", user_create, name='user_create'),
    path("manage/<int:pk>/",user_crud,name="user_crud"),
    path("perms/",manage_perms, name='manage_perms'),
    path('login/', classic_login, name='login'),
    path('logout/', logout_then_login, name='logout'),
    path('permissoes/<int:user_id>/', manage_perms_classic, name='manage_user_perms'),
    path('create_user/',UserCreateModalView.as_view(),name='create_user'),
    path('detail/<int:pk>',UserDetailView.as_view(),name='detail_user'),
    path("edit/<int:pk>/", UserEditView.as_view(), name='user_edit'),
    path('password_reset/', PasswordResetRequestView.as_view(), name='password_reset_request'),
    path('password_reset/<uidb64>/<token>/', PasswordResetView.as_view(), name='password_reset'),
]