# Generated by Django 3.2.9 on 2021-12-03 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=70)),
                ('branch', models.CharField(max_length=250)),
                ('address', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=120, null=True)),
                ('district', models.CharField(blank=True, max_length=120, null=True)),
                ('state', models.CharField(blank=True, max_length=120, null=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.bank')),
            ],
        ),
    ]