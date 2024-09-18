# Generated by Django 4.2.16 on 2024-09-14 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloth', '0003_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
