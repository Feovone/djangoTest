from django.urls import path

from . import views

urlpatterns = [
    path("", views.AtmospherePressureView.as_view(), name='atmosphere_pressure_list'),
    path("<slug:slug>", views.AtmospherePressureDetailView.as_view(), name='atmosphere_pressure_detail'),
    path("create/", views.AtmospherePressureCreateView.as_view(), name='atmosphere_pressure_create'),
    path("export/<int:pk>", views.export, name='atmosphere_pressure_download'),
    path("pdf_list/", views.PdfMakerView.as_view(), name='pdf_list'),
    path("pdf_list/<slug:slug>/", views.PdfMakerDetail.as_view(), name='pdf_detail'),
    path("pdf_create/", views.PdfMakerCreateView.as_view(), name='pdf_create'),
    path("pdf_list/pdf_export/<int:pk>/", views.pdf_export, name='pdf_export'),
    path("secure/", views.index, name="index"),
]
