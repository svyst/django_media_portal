# Generated by Django 2.2.3 on 2019-08-20 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediaportal_app', '0006_article_users_reaction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='dislike',
            new_name='dislikes',
        ),
    ]
