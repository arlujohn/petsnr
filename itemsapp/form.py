from django import forms
from django.contrib.auth.models import User

class ItemsForm(forms.Form):
    item_name = forms.CharField(max_length=64,initial="NA")
    item_description = forms.CharField(max_length=120,initial="NA")
    item_category = forms.CharField(max_length=120,initial="Misc")
    item_price = forms.IntegerField()
    item_stock = forms.IntegerField()


    def add_items(self):
        print(f"Adding the item: {self.cleaned_data['item_name']}")


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput,label="Confirm Password")

    class Meta:
        model = User
        fields = ['username','password','password_confirm']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        #Check if the passwords match
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        else:
            return cleaned_data



class LoginForm(forms.Form):
    username = forms.CharField(max_length=64,initial="NA")
