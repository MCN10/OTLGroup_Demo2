# Generated by Django 3.1.7 on 2021-02-24 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpticTradeLinks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optictradelinksorder',
            name='status',
            field=models.CharField(choices=[('Welcome', 'Welcome'), ('Pending', 'Pending'), ('Payment Confirmed, Processing Order', 'Payment Confirmed, Processing Order'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]