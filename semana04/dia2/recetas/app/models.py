from django.db import models

# Create your models here.}

class Autor(models.Model):
    nombre = models.CharField(max_length=200)
    email = models.EmailField(unique=True, max_length=200)

    def __str__(self):
        return self.nombre
    
    

class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    ingredientes = models.TextField(help_text='redacta los ingredientes')
    preparacion = models.TextField()
    tiempo_registro = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Autor,on_delete=models.RESTRICT)

    def __str__(self):
        return self.titulo
    

class Comentario(models.Model):
    receta = models.ForeignKey(Receta,on_delete=models.CASCADE)
    texto = models.TextField(help_text='redacta tu comentario')
    
    def __str__(self):
        return self.texto