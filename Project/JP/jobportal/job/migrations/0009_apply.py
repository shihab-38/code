# Generated by Django 3.1.3 on 2023-04-01 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_remove_job_vacancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(null=True, upload_to='')),
                ('applydate', models.DateField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.studentuser')),
            ],
        ),
    ]
