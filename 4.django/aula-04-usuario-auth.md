<style>
img{
    box-shadow: rgba(0, 0, 0, 0.35) 0px 5px 15px;
}
.centro{
    text-align: center;
}
</style>

<h1 class="centro">Aula 04</h1>

<h2>1. Usuário não Logado</h2>
Agora que a aplicação está realizando o cadastro, login e logout do sistema, é possível realizar restrições de determinadas páginas, determinados aplicativos. Para esse tipo de restrição, é necessário usar uma validação do usuário autenticado.

Veja abaixo:
<div class="centro">
    <img src="imagens/aula-04/imagem-01.png">
</div>
<br>

Acima, há um destaque no teste de uma autenticação que está sendo realizado na página. Caso um usuário não logado tente acessar a página, ele será redirecionado para a página de login do usuário.
<br><br>

<h2>2. Imagem do Usuário</h2>
Uma vez que os usuários estão sendo cadastrados, eles precisam ser associados às imagens que eles irão realizar upload. Para isso, a classe **Imagem**, criada no arquivo **/galeria/models.py**, tem que  tem que criado uma chave estrangeira com a tabela User.

Veja como ficará a classe com a chave estrangeira:
<div class="centro">
    <img src="imagens/aula-04/imagem-02.png">
</div>
<br>

No código acima, está sendo feita a importação da classe **User** e depois adicionado um novo campo à classe **Imagem**. Veja os parâmetros usados:
- `to`: define a qual tabela tem que ser feita a realação;
- `on_delete`: define o que acontece com o registro na tabela **Imagem** se o usário proprietário for deletado da tabela **User**; nesse caso, todas as imagens relacionadas a ele serão removidos;
- `related_name`: define a qual campo da tabela será feita a FK;

Uma vez alterada a classe, tem que ser realizado novamente os comandos de migração.
```shell
python manage.py makemigrations
```
e
```shell
python manage.py migrate
```
Agora, o novo campo estará presente na tabela **Imagem** e, também, será uma chave estrangeira.

Veja como ficará a tabela:
<div class="centro">
    <img src="imagens/aula-04/imagem-03.png">
</div>
<br>

Por fim, será adicionado um novo campo no **list_filter** no arquivo **/galeria/admin.py**. Dessa forma, será possível filtrar as imagens através do usuário também.
<div class="centro">
    <img src="imagens/aula-04/imagem-04.png">
    <br><br>
    <img src="imagens/aula-04/imagem-04-1.png">
</div>
<br>

<h2>3. Removendo Espaços em Branco</h2>
Na tela de cadastro do usuário, está sendo coletado o nome do usuário. Acontece que deixar o nome do usuário com espaços em branco não é uma boa prática. Para evitar isso, tem que adcionado uma função que realize essa validação.

Veja abaixo como ficará o arquivo **/usuario/forms.py**:
<div class="centro">
    <img src="imagens/aula-04/imagem-05.png">
</div>
<br>

Dentro da classe é criado um método que fará essa limpeza do campo **nome_cadastro**. Repare que o método começa com **clean_**. Esse nome não é aleatório. Usando **clean** juntamente com o nome do campo, faz que ele seja chamado automaticamente quando o formulário é enviado através da página web.

Se o formulário for preenchido agora e enviado com algum espaço entre as palavras no campo **Nome de Cadastro**, nada vai ser mostrado. Mesmo a função levantando uma exceção, a página ainda não foi configurada para exibir qualquer mensagem.

Então, se faz necessário adicionar uma forma de captar e exibir a mensagem de erro. Veja como ficará:
<div class="centro">
    <img src="imagens/aula-04/imagem-06.png">
</div>
<br>

Acima, é adicionado uma tag for do Django para que a mensagem seja exibida. Veja que a variável usada para captar o erro no for interno é a mesma criada pelo for mais externo.
<br><br>

<h2>4. Revalidando a Senha</h2>
Agora, a validação de senhas iguais está sendo feita na função **view_cadastro**, no arquivo **/usuario/views.py**. Veja abaixo o trecho:
<div class="centro">
    <img src="imagens/aula-04/imagem-07.png">
</div>
<br>

Mas, o ideal é que ele seja feito diretamente no formulário. Para essa alteração funcionar, ela terá que ser feita no arquivo **/usuario/forms.py**.

Veja como ficará:
<div class="centro">
    <img src="imagens/aula-04/imagem-08.png">
</div>
<br>

Agora a validação para senhas que não são iguais está sendo feito diretamente na classe que gerencia o formulario. Isso deixa o código muito mais otimizado.

Veja como ficará a função view_cadastro agora:
<div class="centro">
    <img src="imagens/aula-04/imagem-09.png">
</div>
<br><br>

- - - -
<h1 class="centro">Atividade</h1>

- Adicione o que foi aprendido em seus projetos;

