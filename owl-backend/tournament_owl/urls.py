"""
URL configuration for tournament_owl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from django.conf import settings
from django.http import JsonResponse

def favicon(request):
    return HttpResponseRedirect(settings.STATIC_URL + 'owl.svg')

# Root view
def root_view(request):
    return JsonResponse({
        "message": "Welcome to the API! Use the following endpoints to access the API resources:",
        "endpoints": {
            "Tournaments": "/api/tournaments/",
            "Debates": "/api/debates/",
            "API Documentation": "/api/docs/",
        }
    })

urlpatterns = [
    path('favicon.ico', favicon),
    path('', root_view, name='root'),
    path('admin/', admin.site.urls),
    path('api/',include('tournaments.urls'))
]
