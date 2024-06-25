from django import forms


class AuthorForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام نویسنده را وارد کنید', 'class': 'form-control'}),
        label='نام نویسنده'
    )
    image = forms.ImageField(
        widget=forms.FileInput(attrs={'placeholder': 'لطفا تصویر نویسنده را وارد نمایید', 'class': 'form-control'}),
        label='تصویر نویسنده'
    )
