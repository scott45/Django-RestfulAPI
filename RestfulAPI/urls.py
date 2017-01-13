from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from microservice import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fellows/', views.FellowsList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
