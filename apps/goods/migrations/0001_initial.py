# Generated by Django 2.1.4 on 2018-12-21 23:44

import DjangoUeditor.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_sn', models.CharField(default='', max_length=50, verbose_name='goods Id')),
                ('name', models.CharField(max_length=100, verbose_name='goods name')),
                ('click_num', models.IntegerField(default=0, verbose_name='click number')),
                ('sold_num', models.IntegerField(default=0, verbose_name='sold number')),
                ('fav_num', models.IntegerField(default=0, verbose_name='favorite number')),
                ('stock', models.IntegerField(default=0, verbose_name='stock number')),
                ('market_price', models.FloatField(default=0, verbose_name='market price')),
                ('shop_price', models.FloatField(default=0, verbose_name='shop price')),
                ('goods_brief', models.TextField(max_length=500, verbose_name='good description')),
                ('goods_desc', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('ship_free', models.BooleanField(default=True, verbose_name='need shipping fee or not')),
                ('goods_front_image', models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='front page image')),
                ('is_new', models.BooleanField(default=True, verbose_name='is new')),
                ('is_hot', models.BooleanField(default=True, verbose_name='is hot')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
            ],
            options={
                'verbose_name': 'goods',
                'verbose_name_plural': 'goods',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='catagory name', max_length=30, verbose_name='name')),
                ('code', models.CharField(default='', help_text='catarogy code', max_length=30, verbose_name='code')),
                ('desc', models.TextField(default='', help_text='catagory description', verbose_name='')),
                ('category_type', models.IntegerField(choices=[(1, 'CLASS 1'), (2, 'CLASS 2'), (3, 'CLASS 3')], help_text='category level', verbose_name='category level')),
                ('is_tab', models.BooleanField(default=False, help_text='is navigator', verbose_name='is navigator')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
                ('parent_category', models.ForeignKey(blank=True, help_text='parent level', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='goods.GoodsCategory', verbose_name='parent level')),
            ],
            options={
                'verbose_name': 'good catagory',
                'verbose_name_plural': 'good catagory',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategoryBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='brand text', max_length=30, verbose_name='brand name')),
                ('desc', models.TextField(default='', help_text='brand desc', max_length=200, verbose_name='brand desc')),
                ('image', models.ImageField(max_length=200, upload_to='brands/')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='goods.GoodsCategory', verbose_name='category')),
            ],
            options={
                'verbose_name': 'brands',
                'verbose_name_plural': 'brands',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='category'),
        ),
    ]
