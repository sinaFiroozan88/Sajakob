from django import forms
from .models import User


class EditPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'لطفا کلمه عبور فعلی خود را وارد نمایید', 'class': 'form-control'}),
        label='کلمه عبور فعلی'
    )

    token = forms.CharField(
        widget=forms.TextInput(attrs={'style': 'display: none'})
    )


class NewPassword(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'class': 'form-control'}),
        label='کلمه عبور'
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید', 'class': 'form-control'}),
        label='تکرار کلمه عبور'
    )

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_pass = self.cleaned_data.get('re_password')

        if password != re_pass:
            raise forms.ValidationError("کلمه های عبور مغایرت دارند")

        return password


class EditUserForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید', 'class': 'form-control'}),
        label='نام کاربری',
    )

    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا پست الکترونیک خود را وارد نمایید', 'class': 'form-control'}),
        label='پست الکترونیک',
    )

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام را وارد نمایید', 'class': 'form-control'}),
        label='نام',
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام خانوادگی را وارد نمایید', 'class': 'form-control'}),
        label='نام خانوادگی',
    )


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
        label='نام کاربری',
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید'}),
        label='کلمه عبور'
    )

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exists_user = User.objects.filter(username=user_name).exists()
        if not is_exists_user:
            raise forms.ValidationError('کاربری با مشخصات وارد شده وجود ندارد')
        return user_name


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'لطفا نام کاربری خود را وارد نمایید'}),
        label='نام کاربری'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'لطفا ایمیل خود را وارد نمایید'}),
        label='ایمیل'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید'}),
        label='کلمه عبور'
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'لطفا کلمه عبور خود را وارد نمایید'}),
        label='تکرار کلمه عبور'
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        print(email)
        is_exists = User.objects.filter(email=email).exists()
        if is_exists:
            raise forms.ValidationError('این ایمیل تکراری است')
        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        print(user_name)
        is_exists = User.objects.filter(username=user_name).exists()
        if is_exists:
            raise forms.ValidationError("این نام کاربری وجود دارد .")
        return user_name

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_pass = self.cleaned_data.get('re_password')

        if password != re_pass:
            raise forms.ValidationError("کلمه های عبور مغایرت دارند")

        return password
