# Generated by Django 4.1.4 on 2022-12-14 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_rename_email_comment_commentor_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
