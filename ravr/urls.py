from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(),name="homepage"),
    path('about/', views.AboutPage.as_view(),name="aboutpage"),
    path('test/', views.TestPage.as_view(),name="testpage"),
    path('thanks/', views.ThanksPage.as_view(), name="thankspage"),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
