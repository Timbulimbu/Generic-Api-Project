# Generated by Django 4.2.7 on 2023-11-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите полное имя контакта', max_length=122, verbose_name='Полное имя')),
                ('email', models.EmailField(help_text='Введите адрес электронной почты', max_length=122, verbose_name='Адрес электронной почты')),
                ('phone', models.CharField(help_text='Введите номер телефонаконтакта', max_length=12, verbose_name='Номер телефона')),
                ('description', models.TextField(help_text='Введите описание и дополнительную информацию о контакте', verbose_name='Описание')),
            ],
        ),
    ]
