from código_classe_agenda import Agenda

instance = Agenda(input('Olá, pra ter acesso a agenda digital informe seu nome: '))

while True:
    condition = int(input(f"""
Sua agenda digital {instance.nome_user}

1 - Ver contatos
2 - Adicionar Contato
3 - Apagar Contatos
4 - Sair do programa

Informe sua opção: """))

    if condition == 1:
        
        if instance.agenda:
            print('\nContatos Disponíveis\n')
            for k, v in instance.agenda.items():
                print(f'Nome: {k} | Número(s): {v}')
        else:
            print('\nSem contatos existentes')
    
    elif condition == 2:
        print(instance.adicionar_contato(input(f'\n{instance.nome_user}, qual o nome do seu contato: '), int(input(f'Informe o número de telefone da pessoa: '))))

        condition = input(f'\n{instance.nome_contato} possuí um número adicional (s/n)? ').lower()

        if 's' in condition:
            print(instance.adicionar_contato(instance.nome_contato, int(input(f'\nEntão nos informe o outro telefone de {instance.nome_contato}: '))))

        else:
            pass
    
    elif condition == 3:
        print(instance.apagar_contato(input(f'\n{instance.nome_user}, qual o nome do contato que deseja apagar? ')))
        
    elif condition == 4:
        print(f'\nVocê escolheu sair, adeus {instance.nome_user}')
        break