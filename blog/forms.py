from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class ContactForm(forms.Form):
    fullName = forms.CharField(
                widget= forms.TextInput(attrs= {
                    "class":"form-control",
                    "id": "form_full_name",
                    "placeholder": "Your full name.",
                })
                )
    email = forms.EmailField(
                widget= forms.EmailInput(attrs={
                    "class":"form-control",
                    "id": "form_email",
                    "placeholder": "Your email."
                })
                )
    content = forms.CharField(

                widget= forms.Textarea(attrs={
                    "class" : "form-control",
                    'id' : 'form_content',
                    'placeholder': 'Your content'
                })
                )

#FORM VALIDATIONS
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not 'gmail.com' in email:
            raise forms.ValidationError('Email has to be gmail.com ')

        return email
class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(attrs={
        "class": 'form-control',
        'id': 'form_username',
        'placeholder': 'User Name'
    }))
    password = forms.CharField(widget= forms.PasswordInput(attrs={
        'class' : 'form-control',
        'id' : 'form_full_name',
        'placeholder' : 'Password'
    }))


class RegForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'id' : 'username',
        'placeholder' : 'Enter Name'
        }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'id' : 'Email',
        'placeholder' : 'Email'
    }))
    password = forms.CharField(widget= forms.PasswordInput(attrs={
        'class' : 'form-control',
        'id' : 'password',
        'placeholder' : 'Password'
    }))
    password2 = forms.CharField(label='Confirm',widget= forms.PasswordInput(attrs={
        'class' : 'form-control',
        'id' : 'password2',
        'placeholder' : 'Conformation Password'
    }))

    #avoiding duplicate fields
    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        print(qs)
        if qs.exists():
            raise forms.ValidationError('User name already taken')

        return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already existed.")
        return email
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError("Password must match.")

        return data
