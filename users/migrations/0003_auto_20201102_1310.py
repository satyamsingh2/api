# Generated by Django 3.1.2 on 2020-11-02 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201102_1219'),
    ]

    operations = [
        migrations.RenameField(
            model_name='get',
            old_name='uid',
            new_name='zip',
        ),
        migrations.RemoveField(
            model_name='get',
            name='uzip',
        ),
        migrations.AlterField(
            model_name='get',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
