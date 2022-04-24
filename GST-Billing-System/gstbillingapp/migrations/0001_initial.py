
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_address', models.TextField(max_length=600)),
                ('customer_phone', models.CharField(max_length=14)),
                ('customer_gst', models.CharField(max_length=15)),
            ],
        ),
    ]
