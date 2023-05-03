import sys
import time
import pandas as pd
from datetime import datetime
from tkinter import filedialog as fd



# Class para abrir e salvar arquivo .xlsx
class SheetFile():
    def __init__(self):
        self.fileOpen = ''
        self.fileSave = ''

    def setFileOpen(self):
        self.fileOpen = fd.askopenfilename(
            filetypes=[
                ('Arquivos XLSX', '.xlsx')
            ])

    def setFileSave(self):
        self.fileSave = fd.asksaveasfilename(
            filetypes=[
                ('Arquivos XLSX', '.xlsx')
            ])

    def getFileOpen(self):
        return self.fileOpen

    def getFileSave(self):
        return self.fileSave


# Classe para selecionar a tabela
class SheetTable(SheetFile):
    def __init__(self):
        self.path = ''
        self.sheet = ''
        super().__init__()


    def setSheet(self):
        super().setFileOpen()
        self.path = super().getFileOpen()
        if (self.path != ''):
            self.sheet = pd.ExcelFile(self.path).sheet_names
        else:
            pass

    def getSheet(self):
        return self.sheet

    def getPathSheet(self):
        return self.path


# Classe para criar o dataframe
class SheetDf(SheetTable):
    def __init__(self):
        self.df= ''
        self.sheets = ''
        self.path = ''
        super().__init__()

    def setDf(self):
        super().setSheet()

        self.path = super().getPathSheet()
        self.sheets = super().getSheet()
        print('--Tabelas disponíveis--')
        print(*self.sheets, sep="\n")
        self.newDf()

    def newDf(self):
        sheet_name = str(input('Insira o nome da tabela: '))
        if sheet_name in self.sheets:
            if (self.path and self.sheets != ''):
                self.df = pd.read_excel(self.path,
                                   sheet_name=sheet_name,
                                   header=0,
                                   engine='openpyxl',
                                   usecols = 'C:AM')
            else:
                pass
        else:
            print('--Tabela não encontrada, tente novamente--')
            self.newDf()

    def getDf(self):
        return self.df


# Classe para criar o PA
class SheetColumn(SheetDf):
    def __init__(self):
        self.df = ''
        self.fileSave = ''
        super().__init__()

    def editionColumn(self):
        # INICIANDO SELEÇÃO DE TABELA
        super().setDf()
        self.df = pd.DataFrame(data=super().getDf())

        # Atribuindo dataframe a variável
        df = self.df

        # INSERINDO COLUNA
        df.insert(loc=0, column='prd-ident_02', value='03')
        print("* COLUNA DE IDENTIFICAÇÃO INSERIDA")

        # RENOMEANDO COLUNAS PADRÃO BPA
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
            'ORIGEM DAS INFORMAÇÕES': 'prd_org_03',
            'PACIENTE': 'prd_nmpac_30',
            'DATA DE NASCIMENTO': 'prd_dtnasc_08',
            'RAÇA/COR': 'prd_raca_02',
            'ETNIAS': 'prd_etnia_04',
            'NACIONALIDADE': 'prd_nac_03',
            'CODIGO DO SERVIÇO': 'prd_srv_03',
            'CÓDIGO DA CLASSIFICAÇÃO': 'prd_clf_03',
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
        print("* COLUNAS RENOMEADAS PARA O PADRÃO CORRETO")

        # INSERINDO VALORES PADRÕES
        df['prd_cnes_07'] = '6097367'
        df['prd_qt_06'] = '1'
        df['prd_caten_02'] = '1'
        df['prd_org_03'] = 'BPA'
        df['prd_etnia_04'] = ''
        df['prd_nac_03'] = '10'
        df['prd_equipe_seq_08'] = ''
        df['prd_equipe_area_04'] = ''
        df['prd_cnpj_14'] = ''
        df['prd_email_pcnte_40'] = ''
        df['prd_ine_10'] = ''


        # SUBSTITUNDO ALGUNS VALORES NAN
        df['prd_raca_02'].fillna('99', inplace=True)
        df['prd_srv_03'].fillna('135', inplace=True)
        df['prd_clf_03'].fillna('2', inplace=True)
        df['prd_lograd_pcnte_03'].fillna('81', inplace=True)
        df.fillna('', inplace=True)
        print("* VALORES EM BRANCO SUSBTITUIDOS")

        # INVERTENDO DATAS
        df['prd_dtaten_08'] = df['prd_dtaten_08'].dt.strftime('%Y%m%d')
        df['prd_dtnasc_08'] = df['prd_dtnasc_08'].dt.strftime('%Y%m%d')
        print("* DATAS INVERTIDAS")

        # ORDENANDO
        df = df.sort_values(by=['prd_cnsmed_15',
                                'prd_dtaten_08',
                                'prd_pa_10',
                                'prd_cnspac_15',
                                'prd_flh_03',
                                'prd_seq_02'], axis=0, na_position='first')
        print("* ORDENAÇÃO DE LINHAS")

        # CONVERTER FORMATO DAS COLUNAS PARA STRING
        df = df.astype(str, copy=False)

        # REMOVENDO CARACTERES ESPECIAIS
        df['prd_cnes_07'] = df['prd_cnes_07'].str.replace('[^0-9\s]', '', regex=True)
        df['prd_cmp_06'] = df['prd_cmp_06'].str.replace('[^0-9\s]', '', regex=True)
        df['prd_pa_10'] = df['prd_pa_10'].str.replace('[^0-9\s]', '', regex=True)
        df['prd_cnspac_15'] = df['prd_cnspac_15'].str.replace('[^0-9\s]', '', regex=True)
        df['prd_ibge_06'] = df['prd_ibge_06'].str.replace('[^0-9\s]', '', regex=True)
        df['prd_cid_04'] = df['prd_cid_04'].str.replace('[^A-Za-z0-9\s]', '', regex=True)
        df['prd_ldade_03'] = df['prd_ldade_03'].str.replace('[^1-9\s]', '', regex=True)
        df['prd_qt_06'] = df['prd_qt_06'].str.replace('[^1-9\s]', '', regex=True)
        df['prd_caten_02'] = df['prd_caten_02'].str.replace('[^1-9\s]', '', regex=True)
        df['prd_raca_02'] = df['prd_raca_02'].str.replace('[^1-9\s]', '', regex=True)
        df['prd_nac_03'] = df['prd_nac_03'].str.replace('[^1-9\s]', '', regex=True)
        df['prd_srv_03'] = df['prd_srv_03'].str.replace('[^1-9\s]', '', regex=True)
        df['prd_clf_03'] = df['prd_clf_03'].str.replace('[^1-9\s]', '', regex=True)
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
        df['prd_cnspac_15'] = df['prd_cnspac_15'].str.slice(stop=15)
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
        df['prd_ldade_03'] = df['prd_ldade_03'].str.zfill(3)
        df['prd_qt_06'] = df['prd_qt_06'].str.zfill(6)
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

        super().setFileSave()
        self.fileSave = super().getFileSave() + '.xlsx'
        df.to_excel(self.fileSave,
                    sheet_name='DADOS',
                    index=False)

    # SALVANDO ARQUIVO XLSX
    def salveXlsx(self):
        # self.fileSave = super().getFileSave()
        df.to_excel(self.getPathSheet() + 'PA.xlsx',
                    sheet_name='DADOS',
                    index=False)

        print("* CONCLUIDO")

    # SALVANDO ARQUIVO TXT
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
        arquivo = open(self.fileSave + '.txt', 'w')
        df2 = df.apply(''.join, axis=1)
        arquivo.writelines("%s\n" % t for t in df2)


dataFrame = SheetColumn()
dataFrame.editionColumn()


# CRIAR REORDENAÇÃO
# Reeditar classes
# Criar um arquivo separado de 'interface' para controlar fluxo
# Tornar classes enxutas
# Falta criar classe para edição de arquivos
# https://pypi.org/project/inquirer/