from django.forms import ModelForm
from app.models import Register

# Create the form class.
class RegisterForm(ModelForm):
     class Meta:
        model = Register
        fields = ['nome_completo', 'data_de_nascimento', 'cpf', 'rg', 'orgao_exp_rg_paciente',
            'nis','cid','medico_solicitante','cns','idade','sexo','raca_cor',
            'admissao','endereco','codigo_de_logradrouro','n_da_casa','complemento',
            'bairro','municipio','estado_civil','nome_da_mae','cpf_mae',
            'rg_da_mae','rg_ssp_mae','nis_mae','nome_do_pai',
            'cpf_pai','rg_pai','rg_ssp_pai','telefone_bpa',
            'telefone_principal','telefone_adicional','responsavel',
            'doc_responsavel_cpf','rg_responsavel',
            'orgao_exp_responsavel', 'demanda_global']