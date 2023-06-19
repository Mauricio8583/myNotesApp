Projeto que lista e permite ao usuario criar uma agenda online<br>

Este projeto utiliza ReactJs no Frontend e Django, framework de Python no Backend<br>

Link do repositorio frontend: https://github.com/Mauricio8583/myNotesAppFront<br>

Dia 1:<br>
    No arquivo settings.py, dentro da pasta myNotesApp, foi configurado dentro de Installed_apps o uso do ApiConfig, que está dentro do arquivo apps.py da pasta api, para que as rotas criadas em api possam ser utilizadas em myNotesApp<br>
    Criação do ambiente virtual env, sugerido para cada projeto com Django <br>
    Utilizando o django-admin para criar a pasta api, onde irá ser declarada as rotas<br>
    Dentro da pasta api, no arquivo views.py, criada a rota getRoute para testar se a API está funcionando corretamente(OK)<br>
    Após a verificação, criado os primeiros endpoints que serão desenvolvidos mais tarde<br>

Dia 2:<br>
    Criado o model de banco de dados Note que vai armazenar as notas<br>
    Criada as rotas getNotes e getNote que irão mostar os dados inseridos no model<br>
    Criado o superuser na parte admin do django, adaptando a parte admin para o que está inserido na tabela Note aparecer<br>
    Criado o arquivo serializers.py que irá informar como e quais dados de Notes irão aparecer na view<br>

Dia 3:<br>
    Criado o FrontEnd com ReactJs<br>
    Adaptando o FrontEnd para receber os dados de getNotes e getNote da API criada com Django<br>
    Estilização será feita com Styled-Components<br>

Dia 4:<br>
    Configurando o CORS para aceitar requisições de fora do servidor, utilizando django-cors-headers<br>
    Criando as páginas que mostram uma única nota<br>
    Utilizando React-Router-Dom para fazer a navegação entre as páginas<br>

Dia 5:<br>
    Fazendo a aplicação retornar a nota de acordo com o ID enviado por parâmetro<br>
    Criando os primeiros links de navegação com react-router-dom<br>
    Começando a criar a estilização da página<br>

Dia 6:<br>
    Finalizando a estilização das páginas inicial e da nota<br>

Dia 7:<br>
    Criando as rotas de atualizar e excluir nota<br>    

Dia 8:<br>
    Criando a rota para criar nova tarefa<br>
    Neste dia tive a dificuldade com o erro 405 Method not allowed, que estava aparecendo na hora de criar nova tarefa<br>
    e por consequencia, não estava criando, resolvi esse erro após inserir / na url de rota notes/create/<br>