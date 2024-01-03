"""
URL configuration for souravjobs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView),
    path('hyd/',views.HydearbadJobsView),
    path('bng/',views.BangaloreJobsView),
    path('pune/',views.PuneJobsView),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/',views.LogoutView),
    path('signup/',views.SignupForm),
    path('hyddelete/<int:id>',views.HydDeleteRecord),
    path('hydupdate/<int:id>',views.HydUpdateRecord),
    path('bngdelete/<int:id>',views.BangaloreDeleteRecord),
    path('bngupdate/<int:id>',views.BangaloreUpdateRecord),
    path('punedelete/<int:id>',views.PuneDeleteRecord),
    path('puneupdate/<int:id>',views.PuneUpdateRecord),
    path('contact/',views.contact_us_view),
    

]
