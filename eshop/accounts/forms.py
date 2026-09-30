from django import forms
from django.contrib.auth.models import User


class RgisterForm(forms.Form):

    user_name = forms.CharField(max_length=80,widget=forms.TextInput(attrs={
         "class":"form-control form-control-lg"
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
         "class":"form-control form-control-lg"
    }))

    first_name = forms.CharField(max_length=80,widget=forms.TextInput(attrs={
         "class":"form-control form-control-lg"
    }))

    last_name = forms.CharField(max_length=80,widget=forms.TextInput(attrs={
         "class":"form-control form-control-lg"
    }))

    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
        "placeholder":"Enter Your password","class":"form-control form-control-lg"
    }))

    confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control form-control-lg"}))

    def clean_user_name(self):
        user_name=self.cleaned_data["user_name"]
        is_user_exists= User.objects.filter(username=user_name).exists()

        if is_user_exists:
            raise forms.ValidationError("username already exist")
        return user_name
    def clean_email(self):
        email=self.cleaned_data["email"]
        is_email_exists= User.objects.filter(email=email).exists()
    
        if is_email_exists:
            raise forms.ValidationError("email already exist")
        return email

    def clean_confirm_password(self):

        password = self.cleaned_data["password"]
        confirm_password = self.cleaned_data["confirm_password"]

        if password != confirm_password:
            raise forms.ValidationError("passwords do not match")

        elif len(confirm_password) < 8:
            raise forms.ValidationError("passwords too short")

        elif not any(x.isupper() for x in confirm_password):
            raise forms.ValidationError(
                "passwords should have at least one capital letter"
            )

        elif not any(x.islower() for x in confirm_password):
            raise forms.ValidationError(
                "passwords should have at least one lower letter"
            )

        return password