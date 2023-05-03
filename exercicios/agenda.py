
# declaramos a variável da lista fora do while
# para os dados não serem apagados a cada repetição
agenda = []

while True:
    print('====== AGENDA ELETRÔNICA DOS ANOS 90 ====== ')
    print('\t1 - Cadastrar')
    print('\t2 - Listar')
    print('\t3 - Alterar')
    print('\t4 - Apagar')
    print('\t0 - Sair')
    opcao = input('>> ')

    # etapa para cadastrar
    if opcao == '1':
        # criamos a variável que vai guardar os dados do contato
        contato = {}

        nome = input('Digite o nome : ')
        telefone = input('Digite o telefone : ')
        email = input('Digite o e-mail : ')
        data_nasc = input('Digite a data de nascimento : ')

        # dividimos a data de nascimento em uma lista usando o separador '/'
        data_lista = data_nasc.split('/')

        # outras formas de pegar o ano de nascimento
        # data_lista = data_nasc[6] + data_nasc[7] + data_nasc[8] + data_nasc[9]
        # data_lista = data_nasc[6:]
        # data_lista = data_nasc[-4:]
        # data_lista = data_lista[-1]
        # data_lista = data_lista[2]

        # adicionamos os valores no dicionário
        contato['nome'] = nome
        contato['telefone'] = telefone
        contato['email'] = email
        contato['data_nasc'] = data_nasc
        # cálculo da idade em tempo de execução
        contato['idade'] = 2023 - int(data_lista[-1])

        agenda.append(contato)

    # etapa para listar todos os contatos de uma só vez
    elif opcao == '2':
        # teste para agenda ainda sem contatos
        if len(agenda) > 0:
            # mostrando os dados com o while
            indice = 0
            print('Mostrando com WHILE')
            while indice < len(agenda):
                # para ficar mais claro, criamos uma variável com apenas o
                # contato atual, que é um dicionário
                mostra = agenda[indice]
                print(f'Nome : {mostra["nome"]}')
                print(f'Telefone : {mostra["telefone"]}')
                print(f'E-mail : {mostra["email"]}')
                print(f'Data de Nascimento : {mostra["data_nasc"]}')
                print(f'Idade : {mostra["idade"]}\n')
                indice += 1

            print('\nMostrando com FOR')
            for contato in agenda:
                # como o for cria essa variável dinamicamente, não criamos
                # a variável como feito no while, pois agora contato é um
                # dicionário
                print(f'O contato = {contato}')
                print(f'Nome : {contato["nome"]}')
                print(f'Telefone : {contato["telefone"]}')
                print(f'E-mail : {contato["email"]}')
                print(f'Data de Nascimento : {contato["data_nasc"]}')
                print(f'Idade : {contato["idade"]}\n')
        else:
            print('A agenda está vazia!')
    # etapa para alterar o contato
    elif opcao == '3':
        buscar_contato = input('Digite o nome do contato : ')
        # teste para agenda ainda sem contatos
        if len(agenda) > 0:
            # sinalizador se o contato foi encontrado
            achou = False
            for contato in agenda:
                if buscar_contato == contato["nome"]:
                    print('Contato encontrado.')
                    print(f'Antes : {contato}')
                    print('------------------')
                    nome = input('Digite o nome : ')
                    telefone = input('Digite o telefone : ')
                    email = input('Digite o e-mail : ')
                    data_nasc = input('Digite a data de nascimento : ')
                    data_lista = data_nasc.split('/')
                    contato['idade'] = 2023 - int(data_lista[-1])

                    achou = True
                    break

            if not achou:
                print(f'Não encontrei o contato {buscar_contato}')
            else:
                print('Contato alterado com sucesso')
        else:
            print('A agenda está vazia!')
    # etapa para excluir um contato
    elif opcao == '4':
        buscar_contato = input('Digite o nome do contato : ')
        # sinalizador se o contato foi encontrado
        if len(agenda) > 0:
            achou = False
            # para apagar com del, precisamos do índice dele, então usamos a
            # variável indice para guardar o índice do contato atual
            indice = 0
            while indice < len(agenda):
                if buscar_contato == agenda[indice]["nome"]:
                    print('Contato encontrado.')
                    del agenda[indice]
                    achou = True
                    break
                indice += 1

            # mesma operação feita com for
            # for contato in agenda:
            #     if buscar_contato == contato["nome"]:
            #         print('Contato encontrado.')
            #         # outra forma de apagar o contato
            #         agenda.remove(contato)
            #         achou = True
            #         break
            #     indice += 1

            if not achou:
                print(f'Não encontrei o contato {buscar_contato}')
            else:
                print('Contato excluído com sucesso')
        else:
            print('A agenda está vazia')
    elif opcao == '0':
        break
    else:
        print('Opção Inexistente!')
print('Fim da Agenda. Você acabou de perder todos os dados.')
