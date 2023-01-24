# Generated by Django 4.1.5 on 2023-01-23 04:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_alter_pledge_supporter_alter_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='bookmarked_by',
            field=models.ManyToManyField(related_name='bookmarked_projects', to=settings.AUTH_USER_MODEL),
        ),
    ]