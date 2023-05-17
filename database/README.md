# Banco de Dados
##### Documentação e detalhes técnicos de um banco de dados em [MYSQL](https://mariadb.org/)



### TABELA DE CONTEÚDOS
=================
<!--ts-->
* Introdução
* Requisitos
* Projeto
    * Conceitual
    * Lógico
    * Físico
* Regras de Segurança
* Backup, restauração e redundância
* Implementação
<!--te-->


### FERRAMENTAS
 O projeto será desenhado usando o software [MySQL Workbench](https://www.mysql.com/products/workbench/)


### INTRODUÇÃO

Nesse breve documento será detalhado todo o projeto do Banco de Dados, seu objetivo e implementação. Foi escolhido o banco de dados relacional: **MariaBD**, pois além de ser *open source* utiliza o modelo de entidade-relacionamento. Facilitando a busca e geração de relatórios.

O projeto é focado na área médica, atendendo diversas clínicas e guardando dados sensíveis dos usuários e pacientes. Por isso, é crucial apresentar as propriedades **ACID**: atomicidade, consistência, isolamento e durabilidade. Outro fator é garantir a proteção desses dados em conformidade com a **LGPD**(Lei Geral de Proteção de Dados) e outras diretrizes de segurança.

### REQUISITOS

A estrutura básica do projeto é seguinte:
<img alt="Diagrama" title="#Diagrama" src="./assets/diagram_1.png" />
