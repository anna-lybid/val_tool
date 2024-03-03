# Generated by Django 5.0.2 on 2024-03-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0003_goal_delete_bus_remove_product_formula_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_number', models.CharField(max_length=100)),
                ('financed_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('term', models.IntegerField()),
                ('balloon', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monthly_payment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('annual_irr', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]