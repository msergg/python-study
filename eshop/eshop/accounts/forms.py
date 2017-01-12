# coding=utf-8

from django import forms

class LoginForm(forms.Form):
    login = forms.CharField(label='Login')
    passwd = forms.CharField(label='Password', widget=forms.PasswordInput)

