# Generated by Django 5.0.1 on 2024-02-02 08:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBlogs', '0009_blog_post_like_count_blog_post_view_count_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=100)),
                ('c_email', models.EmailField(max_length=100)),
                ('c_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='myBlogs.blog_post')),
            ],
        ),
    ]