# Generated by Django 5.0.3 on 2024-04-18 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_portfolioentry_trade_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell'), ('deposit', 'Cash Deposit'), ('withdrawal', 'Cash Withdrawal')], max_length=10, verbose_name='Transaction Type'),
        ),
    ]
