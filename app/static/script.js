(function(win,doc){
    'use strict';
// verifica o delete do dado
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Deseja mesmo apagar este dado?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }
}) (window,document);

// Função para alternar o modo de tema
function toggleTheme() {
  const body = document.body;
  body.classList.toggle("dark-mode");
}

// Obtém o botão de toggle
const toggleBtn = document.getElementById("toggleBtn");

// Define um listener de evento para o botão
toggleBtn.addEventListener("click", toggleTheme);
