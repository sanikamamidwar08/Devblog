from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "Enter your name",
            "class": "form-control"
        })
    )
    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(attrs={
            "placeholder": "Enter your email",
            "class": "form-control"
        })
    )
    message = forms.CharField(
        label="",
        widget=forms.Textarea(attrs={
            "placeholder": "Write your message...",
            "class": "form-control",
            "rows": 4
        })
    )
