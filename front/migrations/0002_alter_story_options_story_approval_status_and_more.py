# Generated by Django 4.0.5 on 2022-08-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name': 'Story', 'verbose_name_plural': 'Stories'},
        ),
        migrations.AddField(
            model_name='story',
            name='approval_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='story',
            name='pic_1',
            field=models.ImageField(default=None, upload_to='images'),
        ),
        migrations.AddField(
            model_name='story',
            name='pic_2',
            field=models.ImageField(default=None, upload_to='images'),
        ),
        migrations.AddField(
            model_name='story',
            name='pic_3',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]