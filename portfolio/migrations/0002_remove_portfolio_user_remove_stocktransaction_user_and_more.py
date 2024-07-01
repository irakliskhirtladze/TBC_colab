# Generated by Django 5.0.6 on 2024-06-27 14:05

import datetime
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='user',
        ),
        migrations.RemoveField(
            model_name='stocktransaction',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cashbalance',
            name='date_modified',
        ),
        migrations.AlterField(
            model_name='cashtransaction',
            name='transaction_date',
            field=models.DateTimeField(verbose_name='Transaction Date'),
        ),
        migrations.CreateModel(
            name='PortfolioEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_type', models.CharField(max_length=10, verbose_name='Investment Type')),
                ('investment_symbol', models.CharField(default='', max_length=10, verbose_name='Investment Symbol')),
                ('investment_name', models.CharField(default='', max_length=100, verbose_name='Investment Name')),
                ('quantity', models.DecimalField(decimal_places=5, max_digits=10, verbose_name='Investment Quantity')),
                ('average_trade_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Trade Price')),
                ('commissions', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Commission')),
                ('cost_basis', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cost Basis')),
                ('current_price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Current Price')),
                ('current_value', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Current Value')),
                ('profit_loss', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='P&L')),
                ('profit_loss_percent', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='P&L %')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Portfolio Entry',
                'verbose_name_plural': 'Portfolio Entries',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Transaction Date')),
                ('transaction_category', models.CharField(choices=[('stock', 'Stock'), ('crypto', 'Crypto'), ('cash', 'Cash')], max_length=10, verbose_name='Transaction Category')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('symbol', models.CharField(blank=True, max_length=10, null=True, verbose_name='Symbol')),
                ('transaction_type', models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell')], max_length=10, verbose_name='Transaction Type')),
                ('quantity', models.DecimalField(decimal_places=5, max_digits=20, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Quantity')),
                ('trade_price', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Trade Price')),
                ('commission', models.DecimalField(decimal_places=5, max_digits=10, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Commission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
        migrations.DeleteModel(
            name='CryptoTransaction',
        ),
        migrations.DeleteModel(
            name='Portfolio',
        ),
        migrations.DeleteModel(
            name='StockTransaction',
        ),
    ]