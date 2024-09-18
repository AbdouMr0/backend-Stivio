# Generated by Django 4.2.16 on 2024-09-11 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='available_sizes',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('tshirt', 'T-Shirt'), ('jeans', 'Jeans'), ('jacket', 'Jacket'), ('shoes', 'Shoes'), ('tracksuit', 'Tracksuit')], max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
