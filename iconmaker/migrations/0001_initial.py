# Generated by Django 3.1.1 on 2020-09-21 14:50

from django.db import migrations, models
import iconmaker.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IconModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='icon name')),
                ('image', models.ImageField(blank=True, null=True, upload_to=iconmaker.models.get_icon_path, verbose_name='icon image')),
            ],
        ),
    ]
