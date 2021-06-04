# Generated by Django 2.2.23 on 2021-06-02 23:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cxp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cubs_Hist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('casa', models.CharField(max_length=20, unique=True)),
                ('valor', models.FloatField()),
                ('area_min', models.IntegerField()),
                ('area_max', models.IntegerField()),
                ('percent_material', models.DecimalField(decimal_places=2, max_digits=2)),
                ('percent_servico', models.DecimalField(decimal_places=2, max_digits=2)),
                ('uf', models.CharField(max_length=2)),
                ('qtd_pavimentos', models.IntegerField()),
                ('garagem', models.CharField(max_length=20)),
                ('tipo_acabamento', models.CharField(max_length=50)),
                ('possui_orcamento', models.BooleanField()),
                ('versao', models.IntegerField()),
                ('dt_criacao', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='cubs',
            name='casa',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]