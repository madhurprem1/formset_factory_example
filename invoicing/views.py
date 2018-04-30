from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView, UpdateView
from django_tables2 import SingleTableView

from invoicing.forms import NuggetCheckFormset, CommandsForm, \
    ConfigCommandForm, NuggetTextFormSet, CustomerForm, MealForm, NuggetCheckForm
from invoicing.models import Commands, ConfigCommand, Customer, Meal, NuggetCheck
from invoicing.tables import InvoiceTable
from django.views import View


# class ConfigCommandFormView(SuccessMessageMixin, FormView):
#     form_class = ConfigCommandForm
#     template_name = 'config_form.html'
#     success_url = reverse_lazy('invoicing:config_add')
#     success_message = 'The Config comamnd name was created correctly.'

#     def get_context_data(self, **kwargs):
#         print("hi1")
#         context = super(ConfigCommandFormView, self).get_context_data(**kwargs)
#         if self.request.POST:
#             context['formset'] = ConfigCommandFormSet(self.request.POST, prefix='items')
#         else:
#             context['formset'] = ConfigCommandFormSet(prefix='items')
#         print(context)    
#         return context

#     def form_valid(self, form):

#         return self.render_to_response(self.get_context_data(form=form))


class CommandFormView(SuccessMessageMixin, FormView):
    form_class = CommandsForm
    template_name = 'command_form.html'
    success_url = reverse_lazy('invoicing:command_add')
    success_message = 'The comamnd name was created correctly.'

    def get_context_data(self, **kwargs):
        context = super(CommandFormView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = CommandsFormSet(self.request.POST, prefix='items')
        else:
            context['formset'] = CommandsFormSet(prefix='items')
        print(context)    
        return context

    def form_valid(self, form):

        return self.render_to_response(self.get_context_data(form=form))


class NuggetAddFormView(View):
    form_class = NuggetCheckForm
    template_name = 'invoice_form.html'
    success_url = reverse_lazy('invoicing:invoice_list')
    success_message = 'The invoice was created correctly.'
#
#     def get_context_data(self, **kwargs):
#         context = super(InvoiceFormView, self).get_context_data(**kwargs)
#         print(context)
#         if self.request.POST:
#             context['nugget_check_formset'] = NuggetCheckFormSet(self.request.POST, prefix='nugget_check')
#             context['nugget_text_formset'] = NuggetTextFormSet(self.request.POST, prefix='nugget_text')
#         else:
#             context['nugget_check_formset'] = NuggetCheckFormSet(prefix='nugget_check')
#             context['nugget_text_formset'] = NuggetCheckFormSet(prefix='nugget_text')
#         return context
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         print(context)
#
#         nugget_check_formset = context['nugget_check_formset']
#         nugget_text_formset = context['nugget_text_formset']
#         print(nugget_check_formset)
#         print(nugget_text_formset)
#
#         if nugget_check_formset.is_valid() and nugget_text_formset.is_valid():
#
#             # group nugget text form with nugget check form
#             nugget_check_form_list = list(nugget_check_formset.forms)
#
#             from collections import defaultdict
#             grouped_nuggets = defaultdict(list)
#             for nugget_text_form in nugget_text_formset.forms:
#                 grouped_nuggets[nugget_check_form_list[nugget_text_form.nugget_id]].append(nugget_text_form)
#
#             for nugget_check_form, nugget_text_forms in grouped_nuggets.item():
#                 nugget_check = nugget_check_form.save(commit=False)
#                 nugget_check.save()
#
#                 for nugget_text_form in nugget_text_forms:
#                     nugget_text_form.nugget = nugget_check
#                     nugget_text_form.save()
#
#             return super(InvoiceFormView, self).form_valid(form)
#         else:
#             return self.render_to_response(self.get_context_data())
#
#
class InvoiceUpdateView(SuccessMessageMixin, UpdateView):
    model = NuggetCheckForm
    form_class = NuggetCheckForm
    template_name = 'invoice_edit.html'
    success_url = reverse_lazy('invoicing:invoice_list')
    success_message = 'The invoice was edited correctly.'
    #
    # def get_context_data(self, **kwargs):
    #     context = super(InvoiceUpdateView, self).get_context_data(**kwargs)
    #     invoice = self.get_object()
    #     productos = invoice.item_set.all()
    #     if self.request.POST:
    #         context['formset'] = ItemInvoiceUpdateFormSet(self.request.POST, self.request.FILES, prefix='items')
    #     else:
    #         context['formset'] = ItemInvoiceUpdateFormSet(queryset=productos, prefix='items')
    #     return context
    #
    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     formset = context['formset']
    #     total = 0
    #     if formset.is_valid():
    #         invoice = form.save(commit=False)
    #         for item_form in formset.forms:
    #             item = item_form.save(commit=False)
    #             item.invoice = self.get_object()
    #             item.save()
    #             total = item.text_data
    #         formset.save()
    #         invoice.total = total
    #         invoice.save()
    #         return super(InvoiceUpdateView, self).form_valid(form)
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form))


class InvoiceSingleTableView(SingleTableView):
    table_class = InvoiceTable
    queryset = NuggetCheck.objects.all()
    template_name = 'invoice_list.html'


# class CommandsFormView(FormView):
#     form_class = CommandsForm
#     template_name = 'invoice_form.html'
#     # success_url = reverse_lazy('invoicing:invoice_list')
#     success_message = 'The Commands was created correctly.'

#     def get_context_data(self, **kwargs):
#         context = super(CommandsFormView, self).get_context_data(**kwargs)
#         print(context, "++++++++++++++++")


def manage_children(request, customer_id):
    """Edit children and their addresses for a single parent."""

    # customer = get_object_or_404(Customer, id=customer_id)

    # customer = Customer()
    config = ConfigCommand()
    meal = Meal()

    configcommand_form = ConfigCommandForm(instance=config)
    meal_form = MealForm(instance=meal)
    customer = get_object_or_404(Customer, id=customer_id)
    customer_form = CustomerForm(instance=customer)
    if request.method == 'POST':
        print(request.POST)
        print("___________--------======", customer, "___________===========")
        formset = NuggetCheckFormset(request.POST, instance=customer)
        print(formset)
        # print(formset.errors)
        # print(formset.non_form_errors())
        print(formset.is_valid())

        if formset.is_valid():
            print("++++++++++++++++++++++++++++++++++++++++++")
            customer_form = CustomerForm(request.POST)
            nugget = customer_form.save()
            print("Nugget saved")
            for f_form in formset:
                if f_form.is_valid() and f_form.has_changed():
            # for commandform in formset.forms:
                    print('##############')
                    print(f_form.has_changed())
                    formset.save()
                    # command = commandform.save(commit=False)
                    # command.customer = nugget
                    # command.save()
                    # for parameter_form in commandform.nested.forms:
                    #     parameter = parameter_form.save(commit=False)
                    #     parameter.nugget = command
                    #     parameter.save()
                    #
                    # print('save successfulll')



            #print(formset.save())

            print("=====================")
            return redirect('customer_view', customer_id=customer.id)
    else:
        formset = NuggetCheckFormset(instance=customer)

    return render(request, 'invoice_form.html', {
                  'parent': customer,
                  'nugget_check_formset': formset, 'customer_form': customer_form, 'configcommand_form': configcommand_form, 'meal_form': meal_form})
    