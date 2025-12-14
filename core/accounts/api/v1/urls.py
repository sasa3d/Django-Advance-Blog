from django.urls import path  # include رو وقتی واقعاً لازم داشتی اضافه کن  # noqa: F401
from . import views
app_name = "accounts_api_v1"  # اختیاری اما مفید برای namespace

urlpatterns = [
    # Registration
    path("register/", views.RegisterAPIView.as_view(), name="register"),
    # Login
    # path("login/", views.LoginAPIView.as_view(), name="login"),
    # # Logout
    # path("logout/", views.LogoutView.as_view(), name="logout"),
    # # Password Change
    # path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
    # # Password Change Done
    # path("password_change/done/", views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    # # Password Reset
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # # Password Reset Done
    # path("password_reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # # Password Reset Confirm
    # path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # # Password Reset Complete
    # path("reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    # API v1
]
