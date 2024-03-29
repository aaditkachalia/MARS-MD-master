# Generated by Django 2.0.3 on 2018-04-11 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_firstname', models.CharField(max_length=25)),
                ('patient_surname', models.CharField(max_length=30)),
                ('doctor', models.CharField(max_length=25)),
                ('disease_type', models.CharField(max_length=100)),
                ('patient_photo', models.FileField(upload_to='')),
                ('affected_region_photo', models.FileField(upload_to='')),
                ('terminal', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
