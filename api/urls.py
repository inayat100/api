from django.urls import path
from .views import home
urlpatterns = [
    path('api/',home,name="api"),
    # path('api/',resg.as_view(),name="api"),

]