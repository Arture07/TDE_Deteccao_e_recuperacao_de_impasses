<div align="center">
  

  ## TDE 2 - Detecção e Recuperação de Impasses
  
  >
  
</div>

## Link do Youtube
<p align="left">
  <a href="https://www.linkedin.com/in/rafael-eliezer-dantas-botelho-fernandes" target="_blank">
     <img src="https://img.shields.io/badge/LinkedIn-00FFFF?style=for-the-badge&logo=linkedin&logoColor=041B2D" />
  </a>
</p>

## Informações do Grupo
**Nome: Grupo 3**

**Integrantes:**
 * Arthur Kuzma
 * Larissa Adames
 * Rafael Fernandes
   
## 🛠 Linguagem Utilizada
<p align="left">
<img src="https://img.shields.io/badge/Python-2D3E50?style=for-the-badge&logo=python&logoColor=00FFFF" /> 
</p>

## Resumo Breve
<p align="justify">Repositório criado com o intuito de documentar e registar os avanços do desenvolvimento do projeto "TDE 2 - Detecção e recuperação de impasses", atividade realizada na matéria de Performance em Sistemas Ciberfísicos lecionada pelo professor Andrey Cabral Meira. </p>
 
 ### Relatórios de Desenvolvimento

## Relatorio 1
## Relatorio 2
## RELATÓRIO PARTE 3 - DEADLOCK
## 1. INTRODUÇÃO
  DeadLock é um estado em que um sistema pode se encontrar onde um processo em execução (p1) espera um recurso que está sendo mantido por um outro processo em execução (p2), que por sua vez o p2 também está esperando um recurso que está sendo mantido pelo p1, assim causando um ciclo onde nenhum dos processos consegue ser concluído, pois, para serem concluídos, ambos necessitam de um recurso que está em posse do outro.  
  
  Para o DeadLock realmente acontecer, é necessário que quatro condições estejam ocorrendo simultaneamente, essas condições são conhecidas como “Condições de Coffman”, estas são: 
* 1. **Exclusão Mútua -** apenas um processo pode usar um mesmo recurso por vez;
* 2. **Retenção de Recursos -** um processo retêm pelo menos um recurso e ainda assim solicita recursos que estão sendo mantidos por outros processos;
* 3. **Sem preempção -** um recurso só pode ser liberado pelo próprio processo que o detém;
* 4. **Espera Circular -** dois ou mais processos esperam pelo recurso que é mantido pelo próximo processo, onde o último processo depende do recurso do primeiro. Ex: p1 depende de p2 e p2 de p3, mas p3 depende de p1. 2.
    
## 2. DESENVOLVIMENTO 
  No desenvolvimento dessa atividade, foram utilizados os pseudo códigos passados pelo professor para assim identificarmos como prosseguiríamos com a pesquisa. A ideia proposta no próprio texto de apoio foi a de realizar uma hierarquia de recursos, onde para solicitar o recurso Y o processo obrigatoriamente deveria ter solicitado o recurso X antes. O código que foi passado como referência para a situação falha (situação que causava o deadlock)  não permitia a conclusão da execução justamente devido a “falta” de hierarquia de recursos, onde a thread_1 solicitava o recurso “A” ao mesmo tempo em que a thread_2 solicitava o recurso “B”, e ao passarem para o próximo passo que deveriam realizar (thread_1 solicitar B e thread_2 solicitar A), se encontravam em conflito, onde nenhuma thread abria mão de seu recurso e ainda assim solicitava o outro recurso. Durante a execução deste código foram utilizadas as bibliotecas “threading” para a criação e gerência de threads e locks e a biblioteca  “time” para controlar com mais precisão o tempo de execução dos comandos, permitindo assim uma melhor clareza dos fatos. 
  
## 2.2 Evidências de Execução

Código Codigo Funcional: 
![foto-sucesso](img/deadlock-sucesso.png)

Codigo com Falhas:
![foto-erro](img/deadlock-falha.png)
<span style="color:red">Não executava o restante do código devido nenhum dos processos liberarem os recursos. 
</span>

## 3. CONCLUSÃO 
  Para solucionar o estado de deadlock do sistema, foi utilizada uma hierarquia de recursos, assim como proposto na atividade, exigindo que todas as threads solicitassem primeiramente o LOCK_A para que somente após isso pudessem solicitar o LOCK_B, assim quebrando a condição de “espera circular”, pois, a thread A não dependia de um recurso mantido pela thread B nem vice-versa, vale salientar que ordem de execução das threads não interferiu nos resultados de sucesso segundo o observado. Observe também que as condições de “sem preempção”, “exclusão mútua” e “retenção de recursos” não foram quebradas, ou seja, essas condições ainda são válidas no sistema, provando que para que o deadlock realmente ocorra, todas as “Condições de Coffman” precisam ser atendidas . 

 ## Orientações de Execução do Código
* Clone esse repositório normalmente em sua máquina;
* Em sua IDE de preferência (VS code é o recomendado) execute o código;

**OBS:** esse código não necessita de quaisquer outros passos para a sua execução.