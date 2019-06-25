from django import forms

class UserForm(forms.Form):
    username = forms.CharField(label='账号',max_length=128)
    password = forms.CharField(label='密码',max_length=256,widget=forms.PasswordInput)