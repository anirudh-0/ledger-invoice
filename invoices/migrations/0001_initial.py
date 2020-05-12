# Generated by Django 2.2.12 on 2020-05-12 19:23

from django.db import migrations, models
import django.db.models.deletion
import invoices.custom_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('GST_no', models.CharField(max_length=15, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_no', models.IntegerField(primary_key=True, serialize=False)),
                ('date_of_invoice', models.DateField()),
                ('dispatch', models.CharField(max_length=100)),
                ('mode_of_payment', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('state_and_code', models.CharField(max_length=100)),
                ('waybill_no', models.CharField(blank=True, max_length=100)),
                ('sale_items', invoices.custom_fields.SaleItemsListField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('invoice_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='invoices.Party')),
            ],
        ),
    ]