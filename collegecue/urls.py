from django.urls import path # type: ignore
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('register',Register.as_view(),name='register'),
    path('next',Next.as_view(),name="next"),
    path('login',Login.as_view(),name="login"),
    path('forgot',Forgot.as_view(),name="forgot"),
    path('forgot2',Forgot2.as_view(),name="forgot2"),
    path('get-csrf-token/', views.get_csrf_token, name='get_csrf_token'),
    path('register/company/', RegisterCompanyInChargeView.as_view(), name='register_company_incharge_api'),
    path('register/university/', RegisterUniversityInChargeView.as_view(), name='register_university_incharge_api'),
    path('register/consultant/', RegisterConsultantView.as_view(), name='register_consultant_incharge_api'),
    path('search/', views.search, name='search'),
    path('job_portal', Subscriber.as_view(), name='job_portal'),  
    path('verify_otp1',Verify.as_view(),name="verify_otp1"),
    path('resend-otp/', views.resend_otp, name='resend_otp'),
]