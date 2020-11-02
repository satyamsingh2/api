# Generated by Django 3.1.2 on 2020-10-31 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FirstName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LastName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=200)),
                ('fname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.firstname')),
            ],
        ),
    ]