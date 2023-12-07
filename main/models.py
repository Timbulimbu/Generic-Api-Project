from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=122, verbose_name="Полное имя", help_text="Введите полное имя контакта")
    email = models.EmailField(max_length=122, verbose_name="Адрес электронной почты", help_text="Введите адрес электронной почты")
    phone = models.CharField(max_length=12, verbose_name="Номер телефона", help_text="Введите номер телефонаконтакта")
    description = models.TextField(verbose_name="Описание", help_text="Введите описание и дополнительную информацию о контакте")
    
    def __str__(self):
        return self.name
    
 
