from django import forms

class LojaForm(forms.Form):
    nome = forms.CharField(max_length=100, label='nome')
    endereco = forms.CharField(max_length=100, label='endereco')
    telefone = forms.IntegerField(label='telefone')
    image = forms.FileField(label='image')
