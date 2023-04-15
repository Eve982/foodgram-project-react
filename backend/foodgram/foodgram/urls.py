from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('redoc/', TemplateView.as_view(template_name='redoc.html'
    ), name='redoc'),
    path('api/', include('api.urls')),
    path('api/', include('users.urls')),
    
    # path('auth/', include('users.urls', namespace='users')),
    
    # path('auth/', include('django.contrib.auth.urls')),
]