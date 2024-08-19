from django import forms
from .models import User
from phonenumber_field.formfields import PhoneNumberField



class UserForm(forms.ModelForm):
    # phonenumber = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = ['name', 'phonenumber']

    # def clean_phone(self):
    #     phone_number = self.cleaned_data.get("phone_number")
    #     z = phonenumbers.parse(phone_number, "SG")
    #     if not phonenumbers.is_valid_number(z):
    #         raise forms.ValidationError("Number not in SG format")
    #     return phone_number