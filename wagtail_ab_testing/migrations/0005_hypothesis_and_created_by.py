# Generated by Django 3.1.3 on 2020-11-24 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtail_ab_testing', '0004_started_at_and_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='abtest',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='abtest',
            name='hypothesis',
            field=models.TextField(blank=True),
        ),
    ]
