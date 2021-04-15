from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from apps.blog.views import home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('accounts/', include('apps.accounts.urls')),
    path('blog/', include('apps.blog.urls')),
    path('art/', include('apps.art.urls')),
    path('payment/', include('apps.transaction.urls')),
]
0
urlpatterns += [
    path('admin/', admin.site.urls),
    path('account-sns/', include('allauth.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"), name="robots_file"),
    path('sitemap.xml', TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml"), name="sitemap_file"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)