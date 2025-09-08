## O projeto até o monento

#### flask

Microserviço .py para web

Integra ao SQLAlchemy e outro ORMS(Oberjor relacionais ...? )

###### Jinja2:

Gera HTML usando dados do .py

##### Blueprint:

organização do projetos em partes

##### MVC:

model = estrutura dos dados

view = interface do usuário

controller = recebe requisição do usuário, chama model e retorna view

##### Controllers (bllueprint) e padrão MVC:

Organiza as rotas por funcionalidades, tirando as rotas do app,py

#### app.py:

Equivalente ao método public static void main (){} do java

É o file que será procurado para rodar o programa

Flask(__name__): cria a aplicação Flask.

##### docker

imagens = Todas as especificações do serviço: código, dependências, sistema, configurações.Imutável

contêiners = Imagem instânciada,  passa a rodar como serviço ativo, podendo receber requisiões ou executar tarefas.