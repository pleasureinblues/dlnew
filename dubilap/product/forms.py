from django import forms
from django.contrib.auth.models import User
from product.models import ProductProfile, Customer_ps_contact, ModelChoiceField



class Customer_ps_contactForm(forms.ModelForm):

    class Meta:
        model = Customer_ps_contact
        product = forms.ModelChoiceField(queryset=ProductProfile.objects.all(),
widget=forms.HiddenInput())

        fields = ('name','email', 'subject','message', 'phone_number')
        exclude = ['product']


class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    send_a_copy = forms.BooleanField()