# Generated by Django 2.0 on 2018-11-19 19:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0003_auto_20181117_1631'),
        ('user_operation', '0003_auto_20181117_1558'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userfav',
            unique_together={('user', 'goods')},
        ),
    ]
