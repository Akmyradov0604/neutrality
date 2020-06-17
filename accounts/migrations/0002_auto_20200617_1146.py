# Generated by Django 2.2.13 on 2020-06-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='arr_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='arr_flight_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='dep_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='dep_flight_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='email2',
            field=models.EmailField(max_length=60, null=True, unique=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='account',
            name='expiry_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='means_of_transport',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='nda_required',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='office_phone',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='state',
            field=models.CharField(choices=[('Government institution', 'Government institution'), ('Intergovernmental Organization', 'Intergovernmental Organization'), ('NGO', 'NGO'), ('Company', 'Company'), ('Press', 'Press'), ('Other', 'Other')], default='Government institution', max_length=100),
        ),
    ]