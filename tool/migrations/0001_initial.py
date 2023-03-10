# Generated by Django 2.2.12 on 2023-02-27 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PiplineDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(default=None, max_length=30)),
                ('file_type', models.CharField(default=None, max_length=30)),
                ('file_path', models.CharField(default=None, max_length=30)),
                ('schedule_time', models.CharField(default=None, max_length=30)),
                ('table_name', models.CharField(default=None, max_length=30)),
                ('database_name', models.CharField(default=None, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='HiveTableDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=30)),
                ('file_column_name', models.CharField(max_length=30)),
                ('file_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tool.PiplineDetails')),
            ],
        ),
    ]
