"""
URL configuration for VelNote project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include 
from accounts.views import UserCreateView , UserRoleUpdateView , FileUploadView , LoginView , HOME , LogoutView
from rest_framework_simplejwt.views import TokenRefreshView
#from accounts.views import CustomTokenObtainPairView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/signup/', UserCreateView.as_view(), name='user_create'),
    path('update-role/', UserRoleUpdateView.as_view(), name='user_role_update'),
    path('upload-file/', FileUploadView.as_view(), name='file_upload'),
    # path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/home', HOME.as_view(), name='protected'),

]
