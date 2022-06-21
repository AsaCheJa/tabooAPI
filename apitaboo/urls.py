from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateUserAPIView, LogoutUserAPIView
from django.urls import path, re_path
from . import views

urlpatterns = [

    #path('user/', views.UserListView.as_view()),
    #path('user/<str:pk>', views.UserDetailView.as_view()),
    # path('', views.apiOverview, name="api-overview"),
	# path('user-list/', views.userList, name="user-list"),
	# path('user-detail/<str:pk>/', views.userDetail, name="user-detail"),
	# path('user-create/', views.userCreate, name="user-create"),

	# path('user-update/<str:pk>/', views.userUpdate, name="user-update"),
	# path('user-delete/<str:pk>/', views.userDelete, name="user-delete"),

    
    re_path(r'^auth/login/$', obtain_auth_token, name='auth_user_login'),
    re_path(r'^auth/register/$', CreateUserAPIView.as_view(), name='auth_user_create'),
    re_path(r'^auth_user_create/$', LogoutUserAPIView.as_view(), name='auth_user_logout'),
    
    

]

