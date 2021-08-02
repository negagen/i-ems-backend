from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class EnergyCost(models.Model):
    month_year = models.DateField(_("Month"), auto_now=False, auto_now_add=False)
    cost = models.FloatField(_("Cost"))
    trading_company = models.ForeignKey("dataapi.EnergyTradingCompany", verbose_name=_("Energy Trading Company"), on_delete=models.CASCADE)

    class Meta:
        unique_together = ("month_year", "trading_company")

class EnergyTradingCompany(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    sheet_name = models.CharField(_("SpreadSheet"), max_length=50)

