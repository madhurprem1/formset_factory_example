from django.conf.urls import url

from invoicing.views import InvoiceSingleTableView, NuggetAddFormView, InvoiceUpdateView, CommandFormView, manage_children


urlpatterns = [
    url(r'^$', InvoiceSingleTableView.as_view(), name='invoice_list'),
    url(r'^new-invoice/$', NuggetAddFormView.as_view(), name='nugget_add'),
    url(r'^edit-invoice/(?P<pk>\d+)/$$', InvoiceUpdateView.as_view(), name='invoice_edit'),
    url(r'^command-form/$', CommandFormView.as_view(), name='command_add'),
    # url(r'^config-form/$', ConfigCommandFormView.as_view(), name='config_add'),
    url(r'^new-invoice2/(\d+)$', manage_children, name='manage_children'),
]
