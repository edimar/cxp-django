from django.db import models
from django.conf import settings
from django.utils import timezone


class Cubs(models.Model):
	id = models.AutoField(primary_key=True)
	casa = models.CharField(max_length=20, unique=True)
	valor = models.FloatField()
	area_min = models.IntegerField()
	area_max = models.IntegerField()
	percent_material = models.DecimalField(decimal_places=2, max_digits=2)
	percent_servico = models.DecimalField(decimal_places=2, max_digits=2)
	uf = models.CharField(max_length=2)
	qtd_pavimentos = models.IntegerField()
	garagem	= models.CharField(max_length=20)
	tipo_acabamento = models.CharField(max_length=50)
	possui_orcamento = models.BooleanField()

	def publish(self):
		self.save()

	def __str__(self):
		return self.casa

class Cubs_Hist(models.Model):
	id = models.AutoField(primary_key=True)
	casa = models.CharField(max_length=20, unique=True)
	valor = models.FloatField()
	area_min = models.IntegerField()
	area_max = models.IntegerField()
	percent_material = models.DecimalField(decimal_places=2, max_digits=2)
	percent_servico = models.DecimalField(decimal_places=2, max_digits=2)
	uf = models.CharField(max_length=2)
	qtd_pavimentos = models.IntegerField()
	garagem	= models.CharField(max_length=20)
	tipo_acabamento = models.CharField(max_length=50)
	possui_orcamento = models.BooleanField()
	versao = models.IntegerField()
	dt_criacao = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.save()

	def __str__(self):
		return self.casa
