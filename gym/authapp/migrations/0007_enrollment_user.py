# Generated by Django 4.1.1 on 2023-01-19 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authapp', '0006_remove_enrollment_duedate_remove_enrollment_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
