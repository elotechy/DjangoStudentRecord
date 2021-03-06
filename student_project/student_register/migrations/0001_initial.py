# Generated by Django 3.0.2 on 2020-12-02 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('studentID', models.CharField(max_length=5)),
                ('number', models.CharField(max_length=15)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_register.Level')),
            ],
        ),
    ]
