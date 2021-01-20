from django.urls import path
from account.views import SignInView, LogoutView, SignUpView

urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
    # path('api/users/', user_list, name='user_list'),
    # path('api/users/<int:pk>/', user_detail, name='user_detail'),

]

# from django.urls import path
# from account.views import SignInView, LogoutView, SignUpView
# from .api import registration_view
#
# app_name = "account"
#
# urlpatterns = [
#     path('login/', SignInView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     # path('register/', registration_view, name='register'),
#     path('register/', SignUpView.as_view(), name='register'),
#     # path('api/users/', user_list, name='user_list'),
#     # path('api/users/<int:pk>/', user_detail, name='user_detail'),
#
# ]