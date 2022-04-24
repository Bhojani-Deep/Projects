
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gstbillingapp', '0004_auto_20200218_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_name', models.TextField(blank=True, max_length=20, null=True)),
                ('plan_value', models.IntegerField(blank=True, null=True)),
                ('monthly_invoice_limit', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_title', models.TextField(blank=True, max_length=100, null=True)),
                ('business_address', models.TextField(blank=True, max_length=400, null=True)),
                ('business_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('business_phone', models.TextField(blank=True, max_length=20, null=True)),
                ('business_gst', models.TextField(blank=True, max_length=15, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BillingProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan_start_date', models.DateField(blank=True, null=True)),
                ('plan_end_date', models.DateField(blank=True, null=True)),
                ('plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gstbillingapp.Plan')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
