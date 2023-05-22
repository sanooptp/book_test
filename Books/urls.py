from django.contrib import admin
from django.urls import path, include
import Booksapp
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

# router = routers.DefaultRouter()
# router.register(r'users',UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include('userprofile.urls')),
    path('', include("Booksapp.urls")),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]
