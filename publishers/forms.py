from django import forms


class PublisherForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام ناشر را وارد کنید', 'class': 'form-control'}),
        label='نام ناشر'
    )
    logo = forms.ImageField(
        widget=forms.FileInput(attrs={'placeholder': 'لطفا لوگو ناشر را وارد نمایید', 'class': 'form-control'}),
        label='لوگو ناشر'
    )
