# Generated by Django 2.0.7 on 2019-01-30 22:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Jobs', '0006_job_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='author',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]