
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gstbillingapp', '0008_inventory_inventorylog'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorylog',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
