from django.urls import path

from .views import HomeView,EmailView




#register the router 


urlpatterns= [
    path('',HomeView.as_view(),name='index'),
    path('EmailList/',EmailView.as_view(),name='email-list'),
    path('EmailList/<int:pk>',EmailView.as_view(),name='email-by-id'),
]

