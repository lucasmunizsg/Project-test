from django.forms import ModelForm
from app.models import Carros

# Create the form class.
class RegisterForm(ModelForm):
     class Meta:
         model = Carros
         fields = ['NOME COMPLETO',
            'DATA DE NASCIMENTO', 'CPF', 'RG', 'ORGÃO EXP/ RG PACINETE',
            'NIS',
            'CID',
            'MEDICO SOLICITANTE',
            'CNS',
            'IDADE',
            'SEXO',
            'RAÇA/COR',
            'ADMISSÃO',
            'ENDEREÇO',
            'CODIGO DE LOGRADOURO',
            'Nº DA CASA',
            'COMPLEMENTO',
            'BAIRRO',
            'MUNICÍPIO',
            'ESTADO CIVIL',
            'NOME DA MÃE',
            'CPF MÃE',
            'RG DA MÃE',
            'RG SSP MÃE',
            'NIS/MÃE',
            'NOME DO PAI',
            'CPF PAI',
            'RG PAI',
            'RG SSP PAI',
            'TELEFONE BPA',
            'TELEFONE ADICIONAL',
            'TELEFONE 3',
            'RESPONSÁVEL',
            'DOC RESPONSÁVEL CPF',
            'RG RESPONSÁVEL',
            'ORGÃO EXP RESPONSÁVEL']


