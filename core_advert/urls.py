from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns =[
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('inkoranya/', views.inkoranya, name="inkoranya"),
    path('ubukwe/', views.ubukwe, name="ubukwe"),
    path('imbyino/', views.imbyino, name="imbyino"),
    path('ibikoresho/', views.ibikoresho, name="ibikoresho"),
    path('ubuhinzi/', views.ubuhinzi, name="ubuhinzi"),
    path('amasano/', views.amasano, name="amasano"),
    path('indamukanyo/', views.indamukanyo, name="indamukanyo"),
    path('umurage/', views.umurage, name="umurage"),
    path('ikibonezamvugo/', views.ikibonezamvugo, name="ikibonezamvugo"),
    path('amahugurwa/', views.hugura, name="hugura"),
    path('upload/inkoranya/', views.upload_inkoranya, name="upload_inkoranya"),
    path('upload/umurage/', views.upload_umurage, name="upload_umurage"),
    path('upload/amahugurwa/', views.upload_hugura, name="upload_hugura"),
    path('upload/imbyino/', views.upload_imbyino, name="upload_imbyino"),
    path('upload/ubukwe/', views.upload_ubukwe, name="upload_ubukwe"),
    path('upload/ibikoresho/', views.upload_ibikoresho, name="upload_ibikoresho"),
    path('upload/ikibonezamvugo/', views.upload_ikibonezamvugo, name="upload_ikibonezamvugo"),
    path('upload/indamukanyo/', views.upload_indamukanyo, name="upload_indamukanyo"),
    path('upload/amasano/', views.upload_amasano, name="upload_amasano"),
    path('upload/ubuhinzi/', views.upload_ubuhinzi, name="upload_ubuhinzi"),
    path('search/', views.search, name="search"),
    path('admin/', admin.site.urls),
    ]
if settings.DEBUG:
    urlpatterns=urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)