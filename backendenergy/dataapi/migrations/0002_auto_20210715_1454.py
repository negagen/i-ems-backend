# Generated by Django 3.2.5 on 2021-07-15 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyTradingCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('sheet_name', models.CharField(max_length=50, verbose_name='SpreadSheet')),
            ],
        ),
        migrations.AddField(
            model_name='energycost',
            name='trading_company',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dataapi.energytradingcompany', verbose_name='Energy Trading Company'),
            preserve_default=False,
        ),
    ]
