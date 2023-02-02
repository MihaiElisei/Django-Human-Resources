# Generated by Django 3.2.16 on 2023-02-01 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HRApp', '0010_auto_20230201_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='status',
            field=models.CharField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Civil Partnership', 'Civil Partnership'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], default='Single', max_length=17, null=True, verbose_name='Marital Status'),
        ),
    ]
