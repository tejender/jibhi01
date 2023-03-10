# Generated by Django 4.1.4 on 2022-12-21 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='Properties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=200)),
                ('rooms', models.IntegerField()),
                ('price', models.IntegerField()),
                ('host', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.host')),
                ('property_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='listings.categories')),
            ],
        ),
    ]
