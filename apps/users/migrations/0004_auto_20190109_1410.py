# Generated by Django 2.1.4 on 2019-01-09 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181231_1516'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('forum.comments', 'get comments'),), 'verbose_name': 'user Profile', 'verbose_name_plural': 'user Profile'},
        ),
    ]
