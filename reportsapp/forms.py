from django import forms

class UserInputForm(forms.Form):
    user_text = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'テキストを入力'}), label='')