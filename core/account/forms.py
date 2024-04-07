from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    aadhaar_card_text = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    pan_card_text = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    
    aadhaar_card_image = forms.ImageField(required=False)
    pan_card_image = forms.ImageField(required=False)
    proof_of_address_electricity_image = forms.ImageField(required=False)
    income_certificate_image = forms.ImageField(required=False)
    bpl_ration_card_image = forms.ImageField(required=False)


    
    proof_of_address_electricity_text = forms.CharField(
        label="Address Proof Text",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        ),
        required=False
    )
    income_certificate_text = forms.CharField(
        max_length=255,
        required=False,
        label="Income Certificate Text",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )
    bpl_ration_card_text = forms.CharField(
        max_length=255,
        required=False,
        label="Ration Card Text",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )


     

    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2',
                  'aadhaar_card_image', 'pan_card_image', 'proof_of_address_electricity_image',
                  'income_certificate_image', 'bpl_ration_card_image',
                  'aadhaar_card_text', 'pan_card_text', 'proof_of_address_electricity_text',
                  'income_certificate_text', 'bpl_ration_card_text')