# coding=utf-8

from django import forms
from .models import Comment, Product

class CommentForm(forms.Form):
    name = forms.CharField(label='Имя')
    email = forms.EmailField(label='Email')
    comment = forms.CharField(widget=forms.Textarea)

    # ch = forms.ModelChoiceField(queryset=Product.objects.all())

    def clean_comment(self):
        if "abc" in self.cleaned_data['comment']:
            raise forms.ValidationError('abc is not good')
        return self.cleaned_data['comment']




class CommentModelForm(forms.ModelForm):

    class Meta:
        model = Comment

        exclude = ('product',)

