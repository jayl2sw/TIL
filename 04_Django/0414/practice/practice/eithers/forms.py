from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': '제목',

            }
        ),
    )
    blue = forms.CharField(
        widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'ISSUE 1',
            }
        ),
    )
    red = forms.CharField(
    widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder': 'ISSUE 2',
            }
        ),
    )
    
    

    class Meta:
        model = Article
        exclude = ('red_score', 'blue_score', 'vws', 'user')


class CommentForm(forms.ModelForm):

    colors = [
        (True,'BLUE'),
        (False,'RED')
    ]
    color = forms.ChoiceField(choices=colors, widget=forms.Select(attrs={'class':'form-select form-control'}))

    content = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        ),
    )
    
    class Meta:
        model = Comment
        exclude = ('user', 'article',)