# Generated by Django 2.2.28 on 2022-05-13 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.DecimalField(decimal_places=6, max_digits=20)),
                ('per_gm', models.DecimalField(decimal_places=2, max_digits=10)),
                ('buy_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('latest_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('latest_value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('buy_date', models.DateField()),
                ('as_on_date', models.DateField(blank=True, null=True)),
                ('user', models.IntegerField()),
                ('notes', models.CharField(blank=True, max_length=80, null=True)),
                ('goal', models.IntegerField(blank=True, null=True)),
                ('roi', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('buy_type', models.CharField(choices=[('Physical', 'Physical'), ('Other', 'Other'), ('Sovereign Gold Bond Scheme', 'Sovereign Gold Bond Scheme')], max_length=50)),
                ('realised_gain', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('unrealised_gain', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('unsold_weight', models.DecimalField(decimal_places=2, max_digits=20)),
                ('purity', models.CharField(choices=[('22K', '22K'), ('24K', '24K')], default='24K', max_length=10)),
            ],
            options={
                'unique_together': {('buy_date', 'user', 'buy_type', 'weight')},
            },
        ),
        migrations.CreateModel(
            name='SellTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_date', models.DateField()),
                ('notes', models.CharField(blank=True, max_length=40, null=True)),
                ('weight', models.DecimalField(decimal_places=4, max_digits=20)),
                ('per_gm', models.DecimalField(decimal_places=4, max_digits=20)),
                ('trans_amount', models.DecimalField(decimal_places=4, max_digits=20)),
                ('buy_trans', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gold.Gold')),
            ],
            options={
                'unique_together': {('buy_trans', 'trans_date', 'trans_amount')},
            },
        ),
    ]