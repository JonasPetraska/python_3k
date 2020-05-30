# Generated by Django 3.0.6 on 2020-05-30 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='main_member',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='form',
            name='member1',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='member4', to=settings.AUTH_USER_MODEL),
        ),
    ]
