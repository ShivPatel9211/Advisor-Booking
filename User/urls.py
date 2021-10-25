from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/advisor/',views.addAdvisor.as_view()),
    path('user/register/',views.userRegister.as_view()),
    path('user/login/',views.userLogin.as_view()),
    path('user/<int:userId>/advisor/',views.getAdvisor.as_view()),
    path('user/<int:userId>/advisor/<int:advisorId>/',views.bookAdvisor.as_view()),
    path('user/<int:userId>/advisor/booking/',views.getBooking.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
