from django.urls import path, include
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    # media 文件访问路径
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('api/v1/user/', include('user.urls')),
    path('api/v1/course/', include('course.urls')),
    path('api/v1/member/', include('member.urls')),
    path('api/v1/mall/', include('mall.urls')),
]
