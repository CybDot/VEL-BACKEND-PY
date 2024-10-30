from django.urls import path
from .views import UserCreateView, UserRoleUpdateView, FileUploadView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user_create'),
    path('update-role/', UserRoleUpdateView.as_view(), name='user_role_update'),
    path('upload-file/', FileUploadView.as_view(), name='file_upload'),
]
