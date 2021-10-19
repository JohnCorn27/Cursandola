from django import forms
from .models import Page, Categoria, Video

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order', 'categoria' ]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'order': forms.NumberInput(attrs={'class':'form-control'}),
            'categoria': forms.SelectMultiple(attrs={'class' : 'form-control'}),

        }

class PageFormCategoria(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ['title', 'content', 'order', 'video']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control'}),
            'order' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'video' : forms.SelectMultiple(attrs={'class' : 'form-control'}),

        }

class PageFormVideo(forms.ModelForm):

    class Meta:
        model = Video
        fields = ['title', 'content', 'order', 'link']
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'content' : forms.Textarea(attrs={'class' : 'form-control'}),
            'order' : forms.NumberInput(attrs={'class' : 'form-control'}),
            'link' : forms.TextInput(attrs={'class' : 'form-control'}),

        }