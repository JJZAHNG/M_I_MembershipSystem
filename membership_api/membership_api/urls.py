from django.urls import path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    # media 文件访问路径
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT})
]
