# Generated by Django 4.2.6 on 2023-10-27 20:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_remove_cart_name_alter_myuser_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='cart',
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
