# Generated by Django 4.1.4 on 2022-12-16 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cas_blog', '0003_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=200)),
                ('about_person', models.CharField(max_length=200)),
            ],
        ),
    ]
