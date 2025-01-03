from django import forms
from  .models import User 

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'telefone', 'email']

        def __str__(self):
            return f'Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}'
        
class UserFilterForm(forms.Form):
    nome = forms.CharField(required=False, label='nome')
    email = forms.EmailField(required=False, label='email')