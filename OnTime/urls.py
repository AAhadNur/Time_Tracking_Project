
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('user/', include('userprofile.urls')),
    path('myaccount/teams/', include('team.urls')),
    path('projects/', include('project.urls')),
]
