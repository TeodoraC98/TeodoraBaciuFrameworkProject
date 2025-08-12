from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from phonenumber_field.formfields import PhoneNumberField
from django.contrib.auth.models import User
from users.models import User
from django import forms
from .models import Profile


class   UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=' Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control','id':'id_password1'}),
    )
    password2 = forms.CharField(
        label=' Confirm password',
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control','id':'id_password2'}),
    )
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        
        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),

        }
        labels={
            'email': "Email",
            'first_name':'Name',
            'last_name':'Surname',
        }

experience_choice=[
    ("Beggine","Begginer"),
    ("Advanced","Advanced"),
    ("Excelent","Excelent"),
]
class UserProfileForm(forms.ModelForm):
   contact_number= PhoneNumberField()
   experience=forms.ChoiceField(choices=experience_choice,
    widget = forms.Select(
             attrs = {
                'class':'form-control',
                'id':'exp_choice',
            } ))
   class Meta:
        model= Profile
        fields = ['address', 'birth_date','experience']
        widgets = {
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'birth_date':forms.DateInput(format='%Y/%m/%d',attrs={'placeholder': 'YYYY-MM-DD','class':'form-control'}),
        }
        labels={
            'birth_date':"Date of birth:"
        }

       
class   UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))

