from django.shortcuts import render
from django.views.generic import TemplateView
from portfolio_optimization.models import Ticker

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


def search_ticker(request):
    search_text = request.POST.get("search")

    results = Ticker.objects.filter(symbol__icontains=search_text)
    context = {"results": results}
    return render(request, "partials/search-results.html", context)
