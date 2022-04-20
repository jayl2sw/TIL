from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'my-class form-control',
                'placeholder': 'Enter the title',

            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'my-content form-control',

            }
        ),
        error_messages={
            'required':'Please enter your content!!',

        }

    )

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = {'title'}


# class ArticleForm(forms.Form):
#     REGION_A = 'sl'
#     REGION_B = 'dj'
#     REGION_C = 'gj'
#     REGIONS_CHOICE = {
#         (REGION_A, '서울'),
#         (REGION_B, '대전'),
#         (REGION_C, '광주'),
#     }
    
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(widget=forms.Select, choices=REGIONS_CHOICE)