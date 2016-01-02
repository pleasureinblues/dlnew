from django import forms
from django.contrib.auth.models import User
from product.models import ProductProfile, Customer_ps_contact



class Customer_ps_contactForm(forms.ModelForm):

    class Meta:
        model = Customer_ps_contact
        fields = ('name','email','subject','product', 'message', 'phone_number')