
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gstbillingapp', '0006_auto_20200224_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_gst',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
