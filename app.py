from flask import Flask

app = Flask(__name__)

@app.route('/register')
def form():
    return
        <form method="POST" action="/processar">
            <label for="input1">LOCAL DE ATENDIMENTO</label>
            <input type="text" id="atendimento" name="input1"><br><br>
            <label for="input2">MODALIDADE</label>
            <input type="text" id="modalidade" name="input2"><br><br>
            <label for="input3">PACIENTE</label>
            <input type="text" id="paciente" name="input3"><br><br>
            <label for="data">DATA DE ATENDIMENTO</label>
            <input type="date" id="data" name="data"><br><br>
            <label for="input4">CARTÃO SUS</label>
            <input type="text" id="card" name="input4"><br><br>
            <label for="datasince">DATA DE NASCIMENTO</label>
            <input type="date" id="datasince" name="datasince"><br><br>
            <label for="input5">ENDEREÇO</label>
            <input type="text" id="input5" name="input5"><br><br>
            <label for="input6">CID</label>
            <input type="text" id="input5" name="input6"><br><br>
        </form>
