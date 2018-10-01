from django.conf.urls import url
from . import views

app_name = 'vue'
urlpatterns = [
    url(r'^test/', views.hello, name='hello'),

]