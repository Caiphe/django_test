from django import forms


class ClientsForm(forms.ModelForm):
    client_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Client Name',
            'type': 'text'
        }
    ), max_length=100, required=True)

    contact_person = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': "Contact Person",
            'type': 'text'
        }
    ), max_length=100, required=True)

    contact_number = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': "Contact Number",
            'type': 'tel'
        }
    ), max_length=100, required=True)
