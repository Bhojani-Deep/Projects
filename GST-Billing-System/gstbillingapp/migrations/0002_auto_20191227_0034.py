
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gstbillingapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_address',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_gst',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_phone',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.IntegerField()),
                ('invoice_date', models.DateField()),
                ('invoice_json', models.TextField()),
                ('invoice_customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gstbillingapp.Customer')),
            ],
        ),
    ]
