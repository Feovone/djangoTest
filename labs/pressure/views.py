from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.http import HttpResponse, HttpResponseNotFound
from .models import *
import json

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
# Create your views here.


class AtmospherePressureView(ListView):
    '''Полный список'''
    model = AtmospherePressure
    queryset = AtmospherePressure.objects.all()


class AtmospherePressureDetailView(DetailView):
    model = AtmospherePressure
    slug_field = "url"

class AtmospherePressureCreateView(CreateView):
    model = AtmospherePressure
    fields = ('sensor_location', 'date', 'time', 'temperature', 'sensor_name', 'sensor_model', 'url')

def export(request, pk):
    bd = AtmospherePressure.objects.get(id=pk)
    data = {'name': str(bd.sensor_location), 'date': str(bd.date), 'time': str(bd.time), 'temperature': str(bd.temperature), 'sensor_name': str(bd.sensor_name), 'sensor_model': str(bd.sensor_model), 'url': str(bd.url)}
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="members.json"'
    return response


'''PDF'''

class PdfMakerView(ListView):
    model = PdfMaker
    queryset = PdfMaker.objects.all()


class PdfMakerDetail(DetailView):
    model = PdfMaker
    slug_field = "url"

class PdfMakerCreateView(CreateView):
    model = PdfMaker
    fields = ('name', 'time', 'type', 'email', 'url')

def pdf_export(request, pk):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    bd = PdfMaker.objects.get(id=pk)
    p.drawString(100, 50, bd.name)
    p.drawString(100, 100, str(bd.time))
    p.drawString(100, 150, bd.type)
    p.drawString(100, 200, bd.email)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='download.pdf')

    '''Отображение только для авторизованных пользователей'''
def index(request):
    context = {
        'atmospherepressure_list': AtmospherePressure.objects.all()
        if request.user.is_authenticated else []
    }
    return render(request, 'pressure\secure.html', context)
