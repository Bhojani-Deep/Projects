
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gstbillingapp', '0009_inventorylog_last_modified'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_balance', models.FloatField(default=0)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gstbillingapp.Customer')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='product_hsn',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='BookLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('change_type', models.IntegerField(choices=[(0, 'Paid'), (1, 'Purchased Items'), (2, 'Sold Items'), (4, 'Other')], default=0)),
                ('change', models.FloatField(default=0.0)),
                ('description', models.TextField(blank=True, max_length=600, null=True)),
                ('associated_invoice', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gstbillingapp.Invoice')),
                ('parent_book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gstbillingapp.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='last_log',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gstbillingapp.BookLog'),
        ),
        migrations.AddField(
            model_name='book',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
