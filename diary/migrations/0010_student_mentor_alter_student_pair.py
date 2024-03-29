# Generated by Django 4.0.3 on 2022-03-11 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0009_alter_student_pair'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mentor',
            field=models.ManyToManyField(related_name='mentor', to='diary.student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='pair',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='diary.student'),
        ),
    ]
