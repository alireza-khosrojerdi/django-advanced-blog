# from .views import RegisterViewSet, LoginViewSet, LogoutViewSet
from .views import AuthViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("auth", AuthViewSet, basename="auth")
# router.register("register", RegisterViewSet, basename="register")
# router.register("login",LoginViewSet,basename="login")
# router.register("logout",LogoutViewSet,basename="logout")

urlpatterns = router.urls