# Generated by Django 4.0.3 on 2022-03-11 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0013_alter_student_pair'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diary.student'),
        ),
        migrations.RemoveField(
            model_name='student',
            name='pair',
        ),
        migrations.AddField(
            model_name='student',
            name='pair',
            field=models.ManyToManyField(null=True, to='diary.student'),
        ),
    ]