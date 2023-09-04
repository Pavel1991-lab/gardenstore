# Generated by Django 4.2.4 on 2023-09-04 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_product_topic_delete_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('massege', models.TextField(verbose_name='текст')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='тема')),
            ],
        ),
    ]