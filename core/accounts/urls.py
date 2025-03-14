from django.urls import path , include
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'accounts'


urlpatterns = [
    # path('api/' , include('accounts.api.urls')),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.CustomRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout')
]