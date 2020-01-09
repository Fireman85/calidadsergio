from django.shortcuts import render

from django.http import JsonResponse

from cna.models import FactorCna, Caracteristica, Objetivo

def dashboard(request):
    return render(request, 'poa/dashboard.html', {})

def registro_actividad(request):
    factores_coherencia = FactorCna.objects.filter(programa__nombre='Psicologia')
    caracteristicas = Caracteristica.objects.all()
    return render(request,'poa/registro_actividad.html',{ 'factores_coherencia': factores_coherencia, 'caracteristicas': caracteristicas })


def registro_seguimiento(request):
    return render(request,'poa/registro_seguimiento.html',{})


def charts(request):
    return render(request,'poa/charts.html',{})

def tables(request):
    return render(request,'poa/tables.html',{})



#views con peticiones asincronas

def cargar_caracteristicas(request, id_factor):
    caracteristicas = Caracteristica.objects.filter(factor=id_factor).values('id','descripcion')
    return JsonResponse(list(caracteristicas), safe=False)

def cargar_objetivos(request, id_caracteristica):
    objetivos = Objetivo.objects.filter(caracteristica=id_caracteristica).values('id','descripcion')
    return JsonResponse(list(objetivos), safe=False)

