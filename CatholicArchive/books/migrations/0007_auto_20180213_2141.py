# Generated by Django 2.0.2 on 2018-02-14 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ManyToManyField(to='books.Category'),
        ),
    ]
