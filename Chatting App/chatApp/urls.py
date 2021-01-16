
from django.contrib import admin
from django.urls import path, include
from . import views as base_views


from accounts import urls as accounts_urls
from chat import urls as chat_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('personal/', include('personal.urls')),
    path('', base_views.HomePage.as_view(), name='home'),
    path('accounts/', include(accounts_urls)),
    path('chat/', include(chat_urls)),
]
