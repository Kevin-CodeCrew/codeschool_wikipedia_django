# Generated by Django 2.1.1 on 2019-03-10 00:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('d_wiki_app', '0004_auto_20190308_0038'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikipost',
            name='wiki_post_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wikipost',
            name='wiki_post_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/'),
        ),
    ]
