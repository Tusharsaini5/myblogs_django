# Generated by Django 5.0.1 on 2024-02-02 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlogs', '0011_rename_comments_comment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_name',
            new_name='comment_info',
        ),
    ]
