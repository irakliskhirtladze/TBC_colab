# Generated by Django 5.0.3 on 2024-05-07 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_cashtransaction_transaction_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='cash_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cash Balance'),
        ),
    ]
