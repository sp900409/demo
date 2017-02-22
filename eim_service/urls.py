from django.conf.urls import url
import views

urlpatterns = [
    url(r'^status/', views.status_list),
]