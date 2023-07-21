# Trabalho Final #

Construir um website em Django.

## Grupos ##
A turma deve se dividir em grupos de 2 a 3 pessoas (no máximo) de livre escolha. Caso algum integrante de um grupo de duas pessoas desista da disciplina, o aluno que ficar sozinho deve se juntar a outro grupo que possua apenas 2 pessoas.


## Repositório GitHub ##
O GitHub servirá de repositório para o projeto de cada grupo.


Um integrante do grupo ficará responsável por criar o projeto na plataforma. Os demais, deverão realizar um [`fork`](https://docs.github.com/pt/get-started/quickstart/fork-a-repo) do projeto original. Cada integrante deverá trabalhar no seu [`clone do projeto`](https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository).


Após feitas as atualizações, os proprietários do projeto `forkado` deverão realizar um [`pull request`](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) para que suas alterações sejam mescladas com o projeto original.


## Tema do Projeto ##
O tema do projeto é de livre escolha do grupo, sendo vetado os temas de conteúdo apresentado em aula.


## Requisitos para Entrega ##
Abaixo estão listados os requisitos obrigatórios do projeto:
* ter, pelo menos, três aplicativos de sua escolha;
* usar templates globais para mais de um aplicativo;
* ter uma navegabilidade coerente entre todas as páginas do projeto;
* usar a organização de arquivos (templates e static) visto em aula, tanto para aplicativos quanto para o global;
* usar as tags Django:
    * [`if...elif...else`](https://docs.djangoproject.com/pt-br/4.2/ref/templates/builtins/#if)
    * [`for`](https://docs.djangoproject.com/pt-br/4.2/ref/templates/builtins/#for)
    * [`include`](https://docs.djangoproject.com/pt-br/4.2/ref/templates/builtins/#include)
    * [`url`](https://docs.djangoproject.com/pt-br/4.2/ref/templates/builtins/#url)
    * [`static`](https://docs.djangoproject.com/pt-br/4.2/ref/templates/builtins/#static)
    * [`block & extends`](https://docs.djangoproject.com/pt-br/4.2/ref/templates/language/#template-inheritance)
* criar ao menos duas classes em models.py, com os seguintes [`campos`](https://docs.djangoproject.com/pt-br/4.2/topics/db/models/#fields):
    * CharField
    * IntegerField
    * TextField
    * DateTimeField
    * BooleanField
    * ImageField
    * todos os campos não precisam estar presentes ao mesmo tempo em todas as classes, mas o uso de todos é obrigatório;
* usar o banco de dados para guardar os dados inseridos pelo administrador;
* o administrador do projeto deve ter senha e usuário ***admin***;
* usar imagens, CSS e JS nas páginas;
* usar um formulário de busca dentro de algum aplicativo;
* usar cadastro, login e logout de um usuário;
* usar mensagens (do módulo django.contrib) para notificar o usuário;
* permitir ao usuário cadastrar, alterar e apagar algum objeto;
    * usando para isso os formulários específicos de cada um;
* limitar o acesso a determinadas páginas do projeto com base no login do usuário;


## Plágios ##
Plágios não serão permitidos e nem tolerados.
Trabalhos que forem identificados como sendo cópia de outro projeto do GitHub, tutorial do Youtube, tutorial de cursos etc., serão rejeitados e colocará todos os participantes do grupo em recuperação.


## Avaliação ##
O GitHub mantém um registro de todas as contribuições, e isso será usado como um dos critérios de avaliação. Integrantes que tiverem pouca ou nenhuma contribuição (comparado com os demais), irão realizar a recuperação.

Para esse critério, será usado as contribuições individuais de cada projeto.


## Entrega ##
Será feita uma apresentação do projeto com presença obrigatória de todos integrantes do grupo;

Como vai funcionar:
- o grupo irá clonar o projeto do GitHub;
- instalar as dependências a partir do arquivo de **requisitos.txt**;
- executar o projeto;
- apresentar o site e suas funcionalidades;

Critérios avaliados:
- conhecimento do projeto;
- organização dos arquivos e código fonte;
- contribuição ao projeto;
- realização dos requisitos acima descritos;
- apresentação do site;

Após a apresentação, serão feitas perguntas sobre o projeto.

[voltar ao topo](#trabalho-final)
