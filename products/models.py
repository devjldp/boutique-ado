from django.db import models

# Definición del modelo Category
class Category(models.Model):
    # Campo para el nombre de la categoría
    name = models.CharField(max_length=254)
    # Campo opcional para un nombre amigable
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    
    # Método para representar el objeto como una cadena
    def __str__(self):
        return self.name  # Devuelve el nombre de la categoría
    
    # Método para obtener el nombre amigable de la categoría
    def get_friendly_name(self):
        return self.friendly_name

# Definición del modelo Product
class Product(models.Model):
    # Campo para la categoría a la que pertenece el producto (clave externa)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete = models.SET_NULL)
    # Campo para el código SKU del producto
    sku = models.CharField(max_length=254, null=True, blank=True)
    # Campo para el nombre del producto
    name = models.CharField(max_length=254)
    # Campo para la descripción del producto
    description = models.TextField()
    # Campo para el precio del producto
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # Campo para la calificación del producto (opcional)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    # Campo para la URL de la imagen del producto (opcional)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    # Campo para la imagen del producto (opcional)
    image = models.ImageField(null=True, blank=True)

    # Método para representar el objeto como una cadena
    def __str__(self):
        return self.name  # Devuelve el nombre del producto
