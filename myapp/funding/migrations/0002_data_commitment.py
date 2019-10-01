# Generated by Django 2.1.5 on 2019-10-01 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='data_commitment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('fund_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funding.data_fund')),
            ],
        ),
    ]
