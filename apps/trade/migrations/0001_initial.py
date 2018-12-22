# Generated by Django 2.1.4 on 2018-12-22 14:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0004_goodsimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=0)),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods')),
            ],
            options={
                'verbose_name': 'goods in order',
                'verbose_name_plural': 'goods in order',
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sn', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='order id')),
                ('trade_no', models.CharField(blank=True, max_length=100, null=True, verbose_name='trade id')),
                ('pay_status', models.CharField(choices=[('SUCCESS', 'SUCCESS'), ('CLOSED', 'CLOSED'), ('WAIT_PAY', 'WAIT_PAY'), ('FINISHED', 'FINISHED'), ('PAYING', 'PAYING')], default='PAYING', max_length=30, verbose_name='status')),
                ('post_script', models.CharField(max_length=200, verbose_name='message')),
                ('order_mount', models.FloatField(default=0, verbose_name='the quantity')),
                ('pay_time', models.DateTimeField(blank=True, null=True, verbose_name='pay time')),
                ('address', models.CharField(default='', max_length=100, verbose_name='address')),
                ('signer_name', models.CharField(default='', max_length=20, verbose_name='who sign the bill')),
                ('signer_mobile', models.CharField(max_length=20, verbose_name='the phone number')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'order ',
                'verbose_name_plural': 'order ',
            },
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nums', models.IntegerField(default=0, verbose_name='the quantity')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='goods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'shoppingcart',
                'verbose_name_plural': 'shoppingcart',
            },
        ),
        migrations.AddField(
            model_name='order_goods',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='trade.OrderInfo'),
        ),
        migrations.AlterUniqueTogether(
            name='shoppingcart',
            unique_together={('user', 'goods')},
        ),
    ]
