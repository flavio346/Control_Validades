from django.urls import path
from .views import home,my_logout

urlpatterns = [
    path('', home, name="home"),
    path('melogout/', my_logout, name="melogout")
]