# Generated by Django 2.2.2 on 2019-06-08 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
        ('post', '0002_delete_com'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='groups',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='groups.Com'),
            preserve_default=False,
        ),
    ]