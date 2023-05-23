//DISABILITA O BOTÃO SALVAR AO INICIAR A PAGINA
window.onload = function() {
    document.getElementById("save").disabled = true; // Desativa o botão "Salvar" ao carregar a página
  }
  // CHAMA A FUNÇÃO 'DEFINIR DATA ATUAL E DATA DE NASCIMENTO AO CARREGAR A PAGINA' 
  window.addEventListener('DOMContentLoaded', function() {
    definirDataAtual();
    definirDataSince();
  });
  
const changeThemeBtn = document.querySelector("#change-theme");

// DARK AND LIGHT MODE
// Alternar para o modo escuro
function toggleDarkMode() {
  document.body.classList.toggle("dark");
}

// CARREGA O MODO ESTURO OU CLARO 
function loadTheme() {
  const darkMode = localStorage.getItem("dark");

  if (darkMode) {
    toggleDarkMode();
  }
}

loadTheme();

changeThemeBtn.addEventListener("change", function () {
  toggleDarkMode();

  // SALVA OU REMOVE O TEMA SELECIONADO DO LOCALSTORAGE
  localStorage.removeItem("dark");

  if (document.body.classList.contains("dark")) {
    localStorage.setItem("dark", 1);
  }
});
// FIM DA CONFIGURAÇÃO DA FUNÇÃO

// PERMITE SOMENTE COLOCAR A DATA ATUAL NO INPUT 'DATA DE ANTENDIMENTO'
function definirDataAtual() {
    var dataInput = document.getElementById("data");
    
    // Obtém a data atual
    var dataAtual = new Date();
    var ano = dataAtual.getFullYear();
    var mes = ("0" + (dataAtual.getMonth() + 1)).slice(-2); // Adiciona um zero à esquerda para meses menores que 10
    var dia = ("0" + dataAtual.getDate()).slice(-2); // Adiciona um zero à esquerda para dias menores que 10
    
    // Define o valor máximo e mínimo do input como a data atual
    dataInput.setAttribute("max", ano + "-" + mes + "-" + dia);
    dataInput.setAttribute("min", ano + "-" + mes + "-" + dia);
    
    // Define o valor padrão como a data atual
    dataInput.value = ano + "-" + mes + "-" + dia;
  }
// FIM DA CONFIGURAÇÃO DA FUNÇÃO

// PERMITE CADASTRO DE PACIENTES A PARTIR DE UM ANO DE IDADE INPUT 'DATASINCE'
function definirDataSince() {
    var dataInput = document.getElementById("datasince");
    
    // Obtém a data atual
    var dataAtual = new Date();
    
    // Subtrai 1 ano da data atual
    dataAtual.setFullYear(dataAtual.getFullYear() - 1);
    
    var ano = dataAtual.getFullYear();
    var mes = ("0" + (dataAtual.getMonth() + 1)).slice(-2);
    var dia = ("0" + dataAtual.getDate()).slice(-2);
    
    // Define o valor mínimo do input como 1 ano atrás
    dataInput.setAttribute("max", ano + "-" + mes + "-" + dia);
  }
  // FIM DA CONFIGURAÇÃO DA FUNÇÃO

  
// FUNÇÃO QUE NÃO PERMITE A LETRA 'E' NO INPUT NUMBER
function FilterInput(event) {
        var keyCode = ('which' in event) ? event.which : event.keyCode;

        isNotWanted = (keyCode == 69 || keyCode == 101);
        return !isNotWanted;
    };

    function handlePaste (e) {
        var clipboardData, pastedData;

        clipboardData = e.clipboardData || window.clipboardData;
        pastedData = clipboardData.getData('Text').toUpperCase();

        if(pastedData.indexOf('E')>-1) {
            e.stopPropagation();
            e.preventDefault();
        }
};
// FIM DA CONFIGURAÇÃO DA FUNÇÃO

function verificarFormulario() {
    var input1 = document.getElementById("atendimento").value;
    var input2a = document.getElementById("modalidadeA").value;
    var input2b = document.getElementById("modalidadeB").value;
    var input2c = document.getElementById("modalidadeC").value;
    var data = document.getElementById("paciente").value;
    var input3 = document.getElementById("data").value;
    var input4 = document.getElementById("card").value;
    var datasince = document.getElementById("datasince").value;
    var input5 = document.getElementById("endereco").value;
    var input6 = document.getElementById("cid").value;


    
    // Verifica se todos os campos estão preenchidos
    if (input1 !== "" && input2a !== "" && input2b !== "" && input2c !== "" && data !== "" && input3 !== "" && input4 !== "" && datasince !== "" && input5 !=="" && input6 !== "") {
      document.getElementById("save").disabled = false; // Ativa o botão "Salvar"
    } else {
      document.getElementById("save").disabled = true; // Desativa o botão "Salvar"
    }
  }