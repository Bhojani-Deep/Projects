
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gstbillingapp', '0002_auto_20191227_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_hsn', models.CharField(max_length=50)),
                ('product_unit', models.CharField(max_length=50)),
                ('product_gst_percentage', models.FloatField()),
                ('product_rate_with_gst', models.FloatField()),
            ],
        ),
    ]
