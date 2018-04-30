from django import forms
from django.forms import formset_factory, modelformset_factory, Textarea, inlineformset_factory
from django.forms.models import BaseInlineFormSet

from invoicing.models import  NuggetCheck, Commands, ConfigCommand, NuggetText, Customer, Meal


# class InvoiceForm(forms.ModelForm):
#     class Meta:
#         model = Invoice
#         exclude = ['total', 'created', 'modified']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

# class ItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         exclude = ['invoice', 'created', 'modified']
#         widgets = {
#             'title': Textarea(attrs={'cols': 40, 'rows': 10}),
#         }


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        exclude = ['created', 'modified']


class NuggetCheckForm(forms.ModelForm):
    class Meta:
        model = NuggetCheck
        exclude = ['created', 'modified']
        widgets = {
            'command_output': Textarea(attrs={'cols': 40, 'rows': 10}),
        }


class NuggetTextForm(forms.ModelForm):
    class Meta:
        model = NuggetText
        exclude = ['created', 'modified']


class CommandsForm(forms.ModelForm):
    class Meta:
        model = Commands
        exclude = ['created']
        widgets = {
            'name': Textarea(attrs={'cols': 40, 'rows': 10}),
        }


class ConfigCommandForm(forms.ModelForm):
    class Meta:
        model = ConfigCommand
        exclude = ['config_id', 'created']
        widgets = {
            'config_command': Textarea(attrs={'cols': 40, 'rows': 10}),
        }

# ItemInvoiceFormSet = formset_factory(ItemForm, min_num=1, validate_min=True, extra=0, max_num=16, validate_max=True)

# ItemInvoiceUpdateFormSet = modelformset_factory(Item, form=ItemForm, min_num=1, validate_min=True, extra=0,
#                                                 can_delete=True, max_num=16, validate_max=True)


class BaseNuggetFormSet(BaseInlineFormSet):

    def add_fields(self, form, index):
        super(BaseNuggetFormSet, self).add_fields(form, index)

        # save the formset in the 'nested' property
        form.nested = NuggetTextFormSet(
            instance=form.instance,
            data=form.data if form.is_bound else None,
            files=form.files if form.is_bound else None,
            prefix='nugget-text-%s-%s' % (
                form.prefix,
                NuggetTextFormSet.get_default_prefix()))


NuggetCheckFormset = inlineformset_factory(
    Customer, NuggetCheck, form=NuggetCheckForm, formset=BaseNuggetFormSet, extra=1)
NuggetTextFormSet = inlineformset_factory(
    NuggetCheck, NuggetText, fields='__all__',extra=1)
#
#
# NuggetCheckFormSet = formset_factory(Customer, NuggetCheckForm, formset=BaseNuggetFormSet,
#                                      min_num=1, validate_min=True, extra=0, max_num=16, validate_max=True)

# NuggetCheckUpdateFormSet = modelformset_factory(NuggetCheck, form=NuggetCheckForm, min_num=1, validate_min=True, extra=0,
#                                                 can_delete=True, max_num=16, validate_max=True)
#

#
# NuggetTextFormSet = formset_factory(NuggetTextForm, min_num=1, validate_min=True, extra=0, max_num=16, validate_max=True)
#
# NuggetTextUpdateFormSet = modelformset_factory(NuggetTextForm, form=NuggetTextForm, min_num=1, validate_min=True, extra=0,
#                                                 can_delete=True, max_num=16, validate_max=True)

# CommandsFormSet = formset_factory(
#     CommandsForm, min_num=1, validate_min=True, extra=0, max_num=16, validate_max=True)
#
# ConfigCommandFormSet = formset_factory(
#     ConfigCommandForm, min_num=1, validate_min=True, extra=0, max_num=16, validate_max=True)
