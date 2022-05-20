from cProfile import label
import email
from unicodedata import name
from django import forms
from captcha.fields import CaptchaField
from django.core.exceptions import ValidationError


class HoneypotField(forms.BooleanField):
    default_widget = forms.CheckboxInput({
        "style": "display:none !important;",
        "tabindex": "-1",
        "autocomplete": "off"
    })

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", HoneypotField.default_widget)
        kwargs["required"] = False
        super().__init__(*args, **kwargs)

    def clean(self, value):
        if cleaned_value := super().clean(value):
            raise ValidationError("")
        else:
            return cleaned_value


class ContactForm(forms.Form):
    your_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control py-4"}),
        label="Your Name",
        max_length=100,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control py-4"}),
        label="Your email address",
        max_length=150,
    )
    message = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control py-3"}))
    ghtd = HoneypotField()
    captcha = CaptchaField()
