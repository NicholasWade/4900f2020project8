# Generated by Django 3.0.7 on 2020-11-24 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20201124_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='user_full_name',
        ),
    ]
