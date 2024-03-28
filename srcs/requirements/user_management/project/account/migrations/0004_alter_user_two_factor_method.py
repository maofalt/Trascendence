# Generated by Django 5.0.1 on 2024-03-28 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_last_valid_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='two_factor_method',
            field=models.CharField(blank=True, choices=[('', '---------'), ('sms', 'SMS'), ('email', 'Email')], default='', max_length=10, null=True),
        ),
    ]
