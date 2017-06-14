# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = "index.html"
    #def get(self, request, **kwargs):
      #  return render(request, 'index.html', context=None)

# Add about page view
class AboutPageView(TemplateView):
    template_name = "about.html"


# Add portfolio page view
class PortfolioPageView(TemplateView):
    template_name = "portfolio.html"


# Add Contact-us page view
class ContactPageView(TemplateView):
    template_name = "contact.html"
