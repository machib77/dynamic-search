from django.urls import path
from .views import HomePageView
from portfolio_optimization import views

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]

htmx_urlpatterns = [path("search-ticker/", views.search_ticker, name="search-ticker")]

urlpatterns += htmx_urlpatterns
