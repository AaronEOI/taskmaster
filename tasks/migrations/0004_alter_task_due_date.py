# Generated by Django 4.2.1 on 2023-05-12 15:55

from django.db import migrations, models
import tasks.models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, default=None, null=True, validators=[tasks.models.fecha_en_futuro], verbose_name='Fecha de entrega'),
        ),
    ]
