# Generated by Django 2.2.3 on 2019-08-21 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediaportal_app', '0008_useraccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='favorite_articles',
            field=models.ManyToManyField(blank=True, to='mediaportal_app.Article'),
        ),
    ]
