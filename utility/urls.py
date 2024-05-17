from django.urls import path
from . import views
urlpatterns = [
    path("meters/",views.MeterListView.as_view(), name="meter-list-create"),
    path("meters/create/",views.MeterCreateView.as_view(), name="meter-create"),
    path("meter-data/create/",views.MeterDataCreateView.as_view(), name="meter-data-create"),
    path("meters/<int:pk>/",views.MeterDetailsView.as_view(), name="meter-detail")
]