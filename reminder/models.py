from django.db import models

# Create your models here.
class Persona(models.Model):
    """
    Una clase típica definiendo un modelo, derivado desde la clase Model.
    """

    # Campos
    nombre = models.CharField(max_length=20, help_text="Nombre de la persona")
    apellidos = models.CharField(max_length=20, help_text="Apellidos de la persona")
	edad = models.PositiveIntegerField(max_length=20, help_text="Edad de la persona")
	fecha = models.DateField(max_length=20, help_text="Dia y mes del cumpleaños")
    # Metadata
    class Meta: 
        ordering = ["nombre"]

    # Métodos
    def get_absolute_url(self):
         """
         Devuelve la url para acceder a una instancia particular de MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])
    
    #Obligatoria!
    def __str__(self):
        """
        Cadena para representar el objeto Persona (en el sitio de Admin, etc.)
        """
        nombre_completo = self.nombre+" "+self.apellidos
        return nombre_completo
        