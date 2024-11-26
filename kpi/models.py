from django.db import models

# Create your models here.
class KPI(models.Model):
    name = models.CharField(max_length=255)
    expression = models.TextField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class AssetKPI(models.Model): # link
    asset_id = models.IntegerField()
    kpi = models.ForeignKey(KPI, on_delete=models.CASCADE, related_name='assets')

    def __str__(self):
        return f"Asset {self.asset_id} linked to KPI {self.kpi.name}"