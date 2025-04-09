from django.contrib.gis.db import models as gis_models
from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    ref = models.CharField(max_length=100, unique=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    geolocalisation = gis_models.PointField(geography=True, null=True, blank=True)
    vector_search = SearchVectorField(null=True, editable=False)

    def save(self, *args, **kwargs):
        # On calcule le champ géographique à partir de la lat/lon
        if self.latitude and self.longitude:
            from django.contrib.gis.geos import Point
            self.geolocalisation = Point(self.longitude, self.latitude)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom

    class Meta:
        indexes = [
            GinIndex(fields=["vector_search"]),
        ]
