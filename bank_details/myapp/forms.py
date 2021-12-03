from django import forms


class BankDetailsForm(forms.Form):
    ifsc_code = forms.CharField(required=True)

