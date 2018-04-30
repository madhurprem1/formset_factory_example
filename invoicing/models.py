from django.urls import reverse
from django.db import models

TITLE_CHOICES = (
        ('1', 'TEXT'),
        ('2', 'IPV4'),
        ('3', 'IPV6'),
        ('4', 'Boolean'),
        ('5', 'Number'),
    
)
TYPES = (
        ('1', 'PRECHECK'),
        ('2', 'POSTCHECK'),
)

TITLE_OPERATOR = (
        ('1', '>'),
        ('2', '<'),
        ('3', '<='),
        ('4', '>='),
        ('5', '!='),
    
)


# class ModelMeta(models.Model):
#     created = models.DateTimeField('created', auto_now_add=True)
#     modified = models.DateTimeField('modified', auto_now=True)


class Customer(models.Model):
    name = models.CharField('Nugget Name', max_length=255)

    def __str__(self):
        return self.name


# class Invoice(models.Model):
#     name = models.CharField('Nugget Name', max_length=100)
#     # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     total = models.CharField('Total', max_length=100)

#     created = models.DateTimeField('created', auto_now_add=True)
#     modified = models.DateTimeField('modified', auto_now=True)

#     def get_absolute_url(self):
#         return reverse('invoicing:invoice_detail', args=(self.pk,))

class Meal(models.Model):
    primary = models.CharField(max_length=10, choices=TYPES)

    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)


class NuggetCheck(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # command_check = models.ForeignKey(Meal, on_delete=models.CASCADE)

    command_name = models.CharField('Type Command', max_length=100, null=False)
    command_output = models.CharField('Command Output', max_length=5000)

    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)
   

class NuggetText(models.Model):
    nugget = models.ForeignKey(NuggetCheck, on_delete=models.CASCADE, related_name="nugget_texts")
    text_data = models.CharField('TEXT', max_length=100)
    data_type = models.CharField(max_length=10, choices=TITLE_CHOICES)
    data_operator = models.CharField(max_length=10, choices=TITLE_OPERATOR)

    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField('modified', auto_now=True)


class Commands(models.Model):
    name = models.CharField('Command Name', max_length=1000)
    created = models.DateTimeField(auto_now_add=True)


class ConfigCommand(models.Model):
    config_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    config_command = models.CharField('Config Command', max_length=500)
    created = models.DateTimeField(auto_now_add=True)
