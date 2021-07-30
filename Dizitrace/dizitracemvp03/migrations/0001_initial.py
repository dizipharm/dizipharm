# Generated by Django 3.0.4 on 2021-04-10 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction', models.CharField(blank=True, max_length=50, null=True)),
                ('tocken_number', models.CharField(blank=True, max_length=50, null=True)),
                ('current_owner_name', models.CharField(blank=True, max_length=50, null=True)),
                ('order_no', models.CharField(blank=True, max_length=50, null=True)),
                ('product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=50, null=True)),
                ('batch_number', models.CharField(blank=True, max_length=50, null=True)),
                ('mfg_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('customer_no', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_contact', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_gln', models.CharField(blank=True, max_length=50, null=True)),
                ('sscc', models.CharField(blank=True, max_length=50, null=True)),
                ('cost_of_product', models.CharField(blank=True, max_length=50, null=True)),
                ('handoff_timestamp', models.DateField(blank=True, null=True)),
                ('destination', models.CharField(blank=True, max_length=50, null=True)),
                ('designation', models.CharField(blank=True, max_length=50, null=True)),
                ('logistic_name', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.CharField(blank=True, max_length=50, null=True)),
                ('product_category', models.CharField(blank=True, max_length=50, null=True)),
                ('previous_owner_name', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=50, null=True)),
                ('previous_handoff_timestamp', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('packing_type', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_address', models.CharField(blank=True, max_length=50, null=True)),
                ('customer_disease', models.CharField(blank=True, max_length=50, null=True)),
                ('owner_name', models.CharField(blank=True, max_length=50, null=True)),
                ('em_last_updated', models.DateField(blank=True, null=True)),
                ('em_is_active', models.CharField(blank=True, max_length=5, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('instruction', models.CharField(blank=True, max_length=50, null=True)),
                ('mfg_address', models.CharField(blank=True, max_length=50, null=True)),
                ('mfg_name', models.CharField(blank=True, max_length=50, null=True)),
                ('ndc', models.CharField(blank=True, max_length=50, null=True)),
                ('strength', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'ownership',
                'managed': False,
            },
        ),
    ]
