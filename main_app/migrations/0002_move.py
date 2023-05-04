# Generated by Django 4.2 on 2023-04-25 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('element', models.CharField(choices=[('F', 'Fire'), ('W', 'Water'), ('L', 'Lighting')], default='F', max_length=1)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pokemon')),
            ],
        ),
    ]