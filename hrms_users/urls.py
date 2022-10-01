from django.urls import path
from .views import HrmsUserLogin, HrmsUserProfile, HrmsUserChangePassword, SendPasswordResetEmail,  HrmsUserResetPassword

urlpatterns = [
    path('login/', HrmsUserLogin.as_view(), name="login"),
    path('profile/', HrmsUserProfile.as_view(), name="profile"),
    path('changepassword/', HrmsUserChangePassword().as_view(), name="changepassword"),
    path('resetpassword_email/', SendPasswordResetEmail().as_view(), name="resetpassword_email"),
    path('resetpassword/<uid>/<token>/',  HrmsUserResetPassword().as_view(), name="resetpassword"),
]
