
from django.contrib import admin
from django.urls import path ,include
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
urlpatterns = [
    path('djangoAdmin/', admin.site.urls),
    path('',include('User.urls')),
    # path('user/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
