from django.contrib import admin
from django.urls import path
from mainsite.views import homepage, lotto, showpost, mychart


urlpatterns = [
	path('post/<str:slug>/', showpost),
    path('admin/', admin.site.urls),
    path('lotto/', lotto),
    path('mychart/', mychart),
    path('', homepage),
]
