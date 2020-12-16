from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):
    p1=Persona("Profesor Jeison","Fallas")
    temasdelcurso = ["Plantillas","Modelos","fformularios","vistas","Despliegue"]
    #nombre="juan"
    #apellido="Perez"
    ahora=datetime.datetime.now()
    #abrir plantilla en la dirrecion dada
    doc_externo=open("C:/Users/jason/Desktop/Django/proyecto1/proyecto1/plantillas/plantilla.html")
    #objeto template que lee plantilla abierta
    plt=Template(doc_externo.read())
    #cerramos documento
    doc_externo.close()
    #contesto(parametros) en este caso no lleva informacion
    #en el dicionario enviamos el parametro
    ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasdelcurso})
    #rendisar la plantilla
    documento=plt.render(ctx)
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego ")

def damefecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>
    fecha y hora actuales %s
    </h1>
    </boby>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaEdad(request,edad,year):
    periodo=year-2020
    edadFutura=edad+periodo
    documento="<html><boby> En el año %s tendras %s años" %(year, edadFutura)

    return HttpResponse(documento)
