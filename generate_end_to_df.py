import sys
import time
import pandas as pd
from datetime import datetime
from arquivo_abertura_classes import SheetDf


# Editar a Coluna
class SheetColumn(SheetDf):
    def __init__(self):
        super().__init__()
        self.df = ''

    def editionColumn(self):
        # INICIANDO SELEÇÃO DE TABELA

        super().setDf()
        self.df = pd.DataFrame(data=super().getDf())

        # Atribuindo dataframe a variável
        df = self.df

        # INSERINDO COLUNA
        df.insert(loc=0, column='prd-ident_02', value='03')
        print("* COLUNA DE IDENTIFICAÇÃO INSERIDA")

        # RENOMENADO COLUNAS PADRÃO BPA
        df.rename(columns={
            'CNES': 'prd_cnes_07',
            'COMPETENCIA': 'prd_cmp_06',
            'CNS PROFISSIONAL': 'prd_cnsmed_15',
            'CBO': 'cbo_06',
            'DATA DO ATENDIMENTO': 'prd_dtaten_08',
            'Nº FOLHA': 'prd_flh_03',
            'Nº DA LINHA': 'prd_seq_02',
            'CÓDIGO': 'prd_pa_10',
            'CARTÃO SUS': 'prd_cnspac_15',
            'SEXO': 'prd_sexo_01',
            'CÓDIGO IBGE': 'prd_ibge_06',
            'CID': 'prd_cid_04',
            'IDADE': 'prd_ldade_03',
            'QUANTIDADE DE PROCEDIMENTOS PRODUZIDOS': 'prd_qt_06',
            'CARATER DE ATEDIEMENTO': 'prd_caten_02',
            'NÚMERO DA AUTORIZAÇÃO DO ESTABELECIEMENTO': 'prd_naut_13',
            'ORIGEM DAS INFORMAÇÕES	PACIENTE': 'prd_org_03',
            'PACIENTE': 'prd_nmpac_30',
            'DATA DE NASCIMENTO': 'prd_dtnasc_08',
            'RAÇA/COR': 'prd_raca_02',
            'ETNIAS': 'prd_etnia_04',
            'NACIONALIDADE': 'prd_nac_03',
            'CODIGO DO SERVIÇO': 'prd_srv_03',
            'CÓDIGO DA CLISSIFICAÇÃO': 'prd_clf_03',
            'CODIGO DA SEQUENCIA DA EQUIPE': 'prd_equipe_seq_08',
            'CÓDIGO DA AREA DA EQUIPE': 'prd_equipe_area_04',
            'CNPJ': 'prd_cnpj_14',
            'CEP': 'prd_cep_pcnte_08',
            'CODIGO LOGRADOURO': 'prd_lograd_pcnte_03',
            'ENDEREÇO': 'prd_end_pcnte_30',
            'COMPLEMENTO ENDEREÇO': 'prd_compl_pcnte_10',
            'Nº DA CASA': 'prd_num_pcnte_05',
            'BAIRRO': 'prd_bairro_pcnte_30',
            'TELEFONE': 'prd_ddtel_pcnte_11',
            'EMAIL': 'prd_email_pcnte_40',
            'INE': 'prd_ine_10',
            'FIM': 'prd_fim_02'}, inplace=True)
        print("* COLUNAS RENOMEADAS PARA O PADRÃO DO BPA")

        # ORDENANDO
        df = df.sort_values(by=['prd_cnsmed_15',
                                'prd_dtaten_08',
                                'prd_pa_10',
                                'prd_cnspac_15',
                                'prd_flh_03',
                                'prd_seq_02'], axis=0)

        # SUBSTITUNDO ALGUNS VALORES NAN
        df.fillna('', inplace=True)

        # INVERTENDO DATAS
        df['prd_dtaten_08'] = df['prd_dtaten_08'].dt.strftime('%Y%m%d')
        df['prd_dtnasc_08'] = df['prd_dtnasc_08'].dt.strftime('%Y%m%d')
        print("* DATAS INVERTIDAS")

        # CONVERTER FORMATO DAS COLUNAS PARA STRING
        df = df.astype(str, copy=False)

        # REMOVENDO CARACTERES ESPECIAIS
        df['prd_pa_10'] = df['prd_pa_10'].str.replace('[^0-9\s]', '', regex=True)
        df['prd_cnspac_15'] = df['prd_cnspac_15'].str.replace('[^0-9\s]', '', regex=True)
        df['prd_ibge_06'] = df['prd_ibge_06'].str.replace('[^0-9\s]', '', regex=True)
        df['prd_cid_04'] = df['prd_cid_04'].str.replace('[^A-Za-z0-9\s]', '', regex=True)
        df['prd_ldade_03'] = df['prd_ldade_03'].str.replace('[^1-9\s]', '', regex=True)
        df['prd_raca_02'] = df['prd_raca_02'].str.replace('[^1-9\s]', '', regex=True)
        df['prd_lograd_pcnte_03'] = df['prd_lograd_pcnte_03'].str.replace('[^0-9\s]', '', regex=True)
        df['prd_cep_pcnte_08'] = df['prd_cep_pcnte_08'].str.replace('[^0-9\s]', '', regex=True)
        df['prd_num_pcnte_05'] = df['prd_num_pcnte_05'].str.replace('[^0-9\s]', '', regex=True)
        df['prd_ddtel_pcnte_11'] = df['prd_ddtel_pcnte_11'].str.replace('[^0-9\s]', '', regex=True)
        print("* CARACTERES ESPECIAIS REMOVIDOS")

        # LETRAS MAIÚSCULAS E ESPAÇOS EM BRANCOS NAS EXTREMIDADES
        df = df.applymap(lambda x: x.upper(), na_action='ignore')
        df = df.applymap(lambda x: x.strip(), na_action='ignore')
        print("* LETRAS MAIÚSCULAS")

        # CORTE DAS COLUNAS
        df['prd_naut_13'] = df['prd_naut_13'].str.slice(stop=12)
        df['prd_nmpac_30'] = df['prd_nmpac_30'].str.slice(stop=29)
        df['prd_raca_02'] = df['prd_raca_02'].str.slice(stop=2)
        df['prd_lograd_pcnte_03'] = df['prd_lograd_pcnte_03'].str.slice(stop=2)
        df['prd_compl_pcnte_10'] = df['prd_compl_pcnte_10'].str.slice(stop=9)
        df['prd_end_pcnte_30'] = df['prd_end_pcnte_30'].str.slice(stop=29)
        df['prd_bairro_pcnte_30'] = df['prd_bairro_pcnte_30'].str.slice(stop=29)
        df['prd_ddtel_pcnte_11'] = df['prd_ddtel_pcnte_11'].str.slice(stop=10)
        print("* CORTE DE CARACTERES")

        # CARACTERES RESTAMTES
        df['prd_pa_10'] = df['prd_pa_10'].str.zfill(10)
        df['prd_cid_04'] = df['prd_cid_04'].str.ljust(4)
        df['prd_qt_06'] = df['prd_qt_06'].str.zfill(6)
        df['prd_ldade_03'] = df['prd_ldade_03'].str.zfill(3)
        df['prd_caten_02'] = df['prd_caten_02'].str.zfill(2)
        df['prd_naut_13'] = df['prd_naut_13'].str.ljust(13)
        df['prd_nmpac_30'] = df['prd_nmpac_30'].str.ljust(30)
        df['prd_raca_02'] = df['prd_raca_02'].str.zfill(2)
        df['prd_etnia_04'] = df['prd_etnia_04'].str.ljust(4)
        df['prd_nac_03'] = df['prd_nac_03'].str.zfill(3)
        df['prd_srv_03'] = df['prd_srv_03'].str.zfill(3)
        df['prd_clf_03'] = df['prd_clf_03'].str.zfill(3)
        df['prd_equipe_seq_08'] = df['prd_equipe_seq_08'].str.ljust(8)
        df['prd_equipe_area_04'] = df['prd_equipe_area_04'].str.ljust(4)
        df['prd_cnpj_14'] = df['prd_cnpj_14'].str.ljust(14)
        df['prd_lograd_pcnte_03'] = df['prd_lograd_pcnte_03'].str.zfill(3)
        df['prd_end_pcnte_30'] = df['prd_end_pcnte_30'].str.ljust(30)
        df['prd_compl_pcnte_10'] = df['prd_compl_pcnte_10'].str.ljust(10)
        df['prd_num_pcnte_05'] = df['prd_num_pcnte_05'].str.zfill(5)
        df['prd_bairro_pcnte_30'] = df['prd_bairro_pcnte_30'].str.ljust(30)
        df['prd_ddtel_pcnte_11'] = df['prd_ddtel_pcnte_11'].str.zfill(11)
        df['prd_email_pcnte_40'] = df['prd_email_pcnte_40'].str.ljust(40)

        self.df = df

        # SALVANDO ARQUIVO
        super().setFileSave()
        file_save = super().getFileSave()
        df.to_excel(file_save + '.xlsx',
                    sheet_name='DADOS',
                    index=False)

        print("* CONCLUIDO")


    def salveTxt(self):
        df = self.df
        df['prd_pa_10'] = df['prd_pa_10'].str.zfill(10)
        df['prd_cid_04'] = df['prd_cid_04'].str.ljust(4)
        df['prd_qt_06'] = df['prd_qt_06'].str.zfill(6)
        df['prd_ldade_03'] = df['prd_ldade_03'].str.zfill(3)
        df['prd_caten_02'] = df['prd_caten_02'].str.zfill(2)
        df['prd_naut_13'] = df['prd_naut_13'].str.ljust(13)
        df['prd_nmpac_30'] = df['prd_nmpac_30'].str.ljust(30)
        df['prd_raca_02'] = df['prd_raca_02'].str.zfill(2)
        df['prd_etnia_04'] = df['prd_etnia_04'].str.ljust(4)
        df['prd_nac_03'] = df['prd_nac_03'].str.zfill(3)
        df['prd_srv_03'] = df['prd_srv_03'].str.zfill(3)
        df['prd_clf_03'] = df['prd_clf_03'].str.zfill(3)
        df['prd_equipe_seq_08'] = df['prd_equipe_seq_08'].str.ljust(8)
        df['prd_equipe_area_04'] = df['prd_equipe_area_04'].str.ljust(4)
        df['prd_cnpj_14'] = df['prd_cnpj_14'].str.ljust(14)
        df['prd_lograd_pcnte_03'] = df['prd_lograd_pcnte_03'].str.zfill(3)
        df['prd_end_pcnte_30'] = df['prd_end_pcnte_30'].str.ljust(30)
        df['prd_compl_pcnte_10'] = df['prd_compl_pcnte_10'].str.ljust(10)
        df['prd_num_pcnte_05'] = df['prd_num_pcnte_05'].str.zfill(5)
        df['prd_bairro_pcnte_30'] = df['prd_bairro_pcnte_30'].str.ljust(30)
        df['prd_ddtel_pcnte_11'] = df['prd_ddtel_pcnte_11'].str.zfill(11)
        df['prd_email_pcnte_40'] = df['prd_email_pcnte_40'].str.ljust(40)

        super().setFileSave()
        file_save = super().getFileSave()
        arquivo = open(file_save + '.txt', 'w')
        df2 = df.apply(''.join, axis=1)
        arquivo.writelines("%s\n" % t for t in df2)


dataFrame = SheetColumn()
dataFrame.editionColumn()
confirmacao = sheet_name = str(input('Deseja salvar em .txt? (y/n): '))
if confirmacao == 'y':
    dataFrame.salveTxt()
    print('Arquivo Salvo')
else:
    pass
