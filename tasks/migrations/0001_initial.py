# Generated by Django 4.2.1 on 2023-05-11 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='título')),
                ('due_date', models.DateField(default=None, null=True, verbose_name='Fecha de entrega')),
                ('urgent', models.BooleanField(default=False)),
            ],
        ),
    ]
