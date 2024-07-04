from django import forms
from .models import CustomUser
from django.utils.translation import gettext, gettext_lazy as _


class CustomUSerCreationForm(forms.ModelForm):
    password1=forms.CharField(label='password one', widget=forms.PasswordInput)
    password2=forms.CharField(label='password two', widget=forms.PasswordInput)

    class Meta:
        model=CustomUser
        fields=('email',)


        labels={
            'email':_('Email manziligiz')
        }
    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']

        if password1 and password2 and password1 !=  password2:
            raise forms.ValidationError('Parolingiz mos kelmadi')   
        return password2
    
    def save(self,commit=True):
        user=super().save(commit=False),
        user.set_password(self.cleaned_data('password1')),

        if commit:
            user.save()
        return user    


