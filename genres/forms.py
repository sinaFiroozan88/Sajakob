from django import forms


class GenreForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام ژانر را وارد کنید', 'class': 'form-control'}),
        label='نام ژانر'
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'لطفا توضیحات ژانر را وارد نمایید', 'class': 'form-control'}),
        label='توضیحات ژانر'
    )
