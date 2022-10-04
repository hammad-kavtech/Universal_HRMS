from django.urls import path
from .views import HrmsUserLogin, HrmsUserProfile, HrmsUserChangePassword, SendPasswordResetEmail,  HrmsUserResetPassword, HrmsUserLogout #HrmsLogoutAll

urlpatterns = [
    path('login/', HrmsUserLogin.as_view(), name="login"),
    path('logout/', HrmsUserLogout.as_view(), name="logout"),
    path('profile/', HrmsUserProfile.as_view(), name="profile"),
    path('change_password/', HrmsUserChangePassword().as_view(), name="change_password"),
    path('reset_password_email/', SendPasswordResetEmail().as_view(), name="reset_password_email"),
    path('reset_password/<uid>/<token>/',  HrmsUserResetPassword().as_view(), name="reset_password"),
]
