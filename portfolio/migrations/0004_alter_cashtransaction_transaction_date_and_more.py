# Generated by Django 5.0.3 on 2024-04-30 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_cashtransaction_commission_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashtransaction',
            name='transaction_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Transaction Date'),
        ),
        migrations.AlterField(
            model_name='cryptotransaction',
            name='transaction_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Transaction Date'),
        ),
        migrations.AlterField(
            model_name='stocktransaction',
            name='transaction_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Transaction Date'),
        ),
    ]
