import flask from Flask, request

app = Flask(__name__)
@app.route('/register')
def formSave():
@app.route('/processar', methods=['POST'])
def processar():
    input1 = request.form['input1']
    input2 = request.form['input2']
    input3 = request.form['input3']
    data = request.form['data']
    input4 = request.form['input4']
    datasince = request.form['datasince']
    input5 = request.form['input5']
    input6 = request.form['input6']

    print('LOCAL DE ATENDIMENTO', input1)
    print('MODALIDADE', input2)
    print('PACIENTE', input3)
    print('DATA DE ATENDIMENTO', data)
    print('CARTÃO SUS', input4)
    print('DATA DE NASCIMENTO', datasince)
    print('ENDEREÇO', input5)
    print('CID', input6)

    return 'Dados do formulário salvos com sucesso!'
