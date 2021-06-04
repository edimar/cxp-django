# Generated by Django 2.2.23 on 2021-06-02 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cubs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('casa', models.CharField(max_length=20)),
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
            ],
        ),
    ]