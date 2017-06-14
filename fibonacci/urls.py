from django.conf.urls import url
from fibonacci import views

urlpatterns = [
    url(r'^fibonachi', views.fibonacci_request),
]
