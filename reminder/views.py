from django.shortcuts import render
from .models import Persona
# Create your views here.
def index(request):#la funcion que llamamos desde el mapeador url de reminder
    """
    Función para generar la vista del index
    """
    #Obtencion del numero de registros (personas)
    num_personas = Persona.objects.all().count()
    
    
    #Hacemos el render de la lantilla html añadiendo los datos mediante la variable context que es un diccionario que contiene los datos con su marcador
    return render(request,'index.html',
                  context = {'num_personas':num_personas,}
                  )
