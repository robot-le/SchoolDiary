# Generated by Django 4.0.3 on 2022-03-11 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0010_student_mentor_alter_student_pair'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diary.group'),
        ),
        migrations.AlterField(
            model_name='student',
            name='mentor',
            field=models.ManyToManyField(null=True, related_name='mentor', to='diary.student'),
        ),
    ]