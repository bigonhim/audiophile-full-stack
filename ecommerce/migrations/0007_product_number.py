# Generated by Django 5.0.2 on 2024-06-28 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_alter_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
