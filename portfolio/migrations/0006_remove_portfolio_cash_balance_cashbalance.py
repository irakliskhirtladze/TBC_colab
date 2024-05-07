# Generated by Django 5.0.3 on 2024-05-07 19:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_portfolio_cash_balance'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='cash_balance',
        ),
        migrations.CreateModel(
            name='CashBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_modified', models.DateField(auto_now=True, verbose_name='Date Modified')),
                ('cash_balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Cash Balance')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Cash Balance',
                'verbose_name_plural': 'Cash Balances',
            },
        ),
    ]