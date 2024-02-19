from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput({'placeholder': "گذرواژه فعلی", 'name': "old_password"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput({'placeholder': "گذرواژه جدید", 'name': "new_password1"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput({'placeholder': "تکرار گذرواژه", 'name': "new_password2"}))

    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError("گذرواژه فعلی تان اشتباه وارد شد. لطفا دوباره تلاش کنید")
        return old_password


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'is_active', 'is_superuser', 'is_staff')
