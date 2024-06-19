# Generated by Django 5.0.6 on 2024-06-19 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='عنوان')),
                ('pages', models.IntegerField(verbose_name='تعداد صفحات')),
                ('cover', models.ImageField(upload_to='books/', verbose_name='عکس')),
            ],
        ),
    ]
