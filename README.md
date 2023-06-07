Projeto que lista e permite ao usuario criar uma agenda online<br>

Este projeto utiliza ReactJs no Frontend e Django, framework de Python no Backend<br>

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