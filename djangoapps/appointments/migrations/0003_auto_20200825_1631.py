# Generated by Django 3.0.7 on 2020-08-25 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_add_description_and_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeslot_timestamp', models.DateTimeField()),
                ('num_appointments_per_slot', models.IntegerField(default=5)),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='description',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='title',
        ),
        migrations.AddField(
            model_name='appointment',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='test',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='appointments.Test'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='time_slot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='appointments.TimeSlot'),
        ),
    ]