from django import forms

class NoticeForm(forms.Form):
    noticename = forms.CharField(max_length=20,
    widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Notice',
        'id': 'inputName'
    }))

    noticedesc = forms.CharField(widget=forms.Textarea({
        'class': 'form-control',
        'rows': 'Details',
        'placeholder': 'Details'

    }))
