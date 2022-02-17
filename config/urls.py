
import imp
from re import I
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('login/', include("django.contrib.auth.views.login", {'template_name': 'login.html'})),
    # path('logout/', include("django.contrib.auth.views.logout", {'next_page': '/login/'})),
    # path('', include("django.contrib.auth.urls")),
    path('', include("apps.users.urls")),
    path('', include("apps.main.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)