# howdy/urls.py

from django.conf.urls import url
from howdy import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
    url(r'^portfolio/$', views.PortfolioPageView.as_view()),  # Add this /portfolio/ route
    url(r'^contact/$', views.ContactPageView.as_view()),  # Add this /contact page/ route

]