from django import forms
from apps.user.models import User
import re
from hashlib import md5


class UserForm(forms.Form):
    username = forms.CharField(label='账号',max_length=128)
    password = forms.CharField(label='密码',max_length=256,widget=forms.PasswordInput)


USERNAME_PATTREN=re.compile(r'\w{4,20}')

class RegisterForm(forms.ModelForm):
    repassword=forms.CharField(min_length=8,max_length=20)

    def clean_username(self):
        username=self.cleaned_data['username']
        if not USERNAME_PATTREN.fullmatch(username):
            raise ValidationError('用户名由字母、数字和下划线构成且长度为4-20个字符')
        return username
    
    def clean_password(self):
        password=self.cleaned_data['password']
        if len(password) < 8 or len(password) > 20:
            raise ValidationError('无效的密码，密码长度为8-20个字符')
        return to_md5_hex(self.cleaned_data['password'])

    def clean_repassword(self):
        repassword = to_md5_hex(self.celaned_data['repassword'])
        if repassword != self.cleaned_data['password']:
            raise validationError('密码和确认密码不一致')
        return repassword
    
    class Meta:
        model = User
        exclude=('',)

def to_md5_hex(message):
    return md5(message.encode()).hexdigest()