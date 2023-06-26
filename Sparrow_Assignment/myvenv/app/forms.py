from django import forms
from .models import Purchase, PurchaseDetails

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['invoice_no', 'invoice_date', 'supplier', 'total_amount']

class PurchaseDetailsForm(forms.ModelForm):
    class Meta:
        model = PurchaseDetails
        fields = ['item', 'quantity', 'price', 'amount','purchase_master']

PurchaseDetailsFormset = forms.inlineformset_factory(
    Purchase, PurchaseDetails, form=PurchaseDetailsForm, extra=1
)
