from .models import User
from django import forms


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput()
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ["username","email","password"]

    def clean(self):
        cleaned_data = super().clean()

        self.password = cleaned_data.get("password")
        self.confirm_password = cleaned_data.get("confirm_password")

        if self.password != self.confirm_password:
            raise forms.ValidationError(
                "Passwords do not match."
            )
        
        return cleaned_data
    


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())