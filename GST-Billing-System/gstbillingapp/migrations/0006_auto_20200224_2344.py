
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gstbillingapp', '0005_billingprofile_plan_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='business_gst',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='business_phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='business_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
