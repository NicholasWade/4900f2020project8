# Generated by Django 3.0.7 on 2020-12-16 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='category',
            new_name='Category',
        ),
    ]
