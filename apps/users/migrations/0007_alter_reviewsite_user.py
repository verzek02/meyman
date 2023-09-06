# Generated by Django 4.2.3 on 2023-09-06 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewsite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
