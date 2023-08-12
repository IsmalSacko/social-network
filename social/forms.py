from django import forms
from .models import Post, Comment, MessageModel


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class PostForm(forms.ModelForm, ):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'rows': '3', 'placeholder': 'Dites quelque chose...'}))
    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={"multiple": True, 'class': 'form-control'})
    )

    class Meta:
        model = Post
        fields = ['body', 'image']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Dites quelque chose...'
        }))

    class Meta:
        model = Comment
        fields = ['comment']


class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)


class MessageForm(forms.ModelForm):
    body = forms.CharField(label='Message', max_length=1000)

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={"multiple": True})
    )

    class Meta:
        model = MessageModel
        fields = ['body']


class ShareForm(forms.Form):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Dites quelque chose...'
        }))


class ExploreForm(forms.Form):
    query = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={
            'placeholder': 'Rechercher avec un hashtag'
        })
    )


