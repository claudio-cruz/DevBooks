# Generated by Django 3.2.16 on 2022-11-19 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devbooksapp', '0003_auto_20221119_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.IntegerField(choices=[(0, 'Finance'), (1, 'Spiritual'), (2, 'Health'), (3, 'Leaderships'), (4, 'Biographies')]),
        ),
    ]
