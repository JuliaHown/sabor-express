import os

restaurantes = [
    {'nome': 'Burger King', 'categoria': 'Fast Food', 'ativo': False},
    {'nome': 'Spoletto', 'categoria': 'Italiana', 'ativo': False},
    {'nome': 'Outback', 'categoria': 'Australiana', 'ativo': True}
]


def exibir_nome_do_programa():
    ''' Exibe o nome estilizado do programa na tela '''
    
    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░      
""")

def exibir_opcoes():
    ''' Exibe as opções disponíveis no menu principal '''

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar/desativar restaurante')
    print('4. Sair\n')

def finalizar_app(): 
    ''' Exibe mensagem de finalização do aplicativo '''
    exibir_subtitulo('Encerrando o programa...')

def opcao_invalida():
    ''' Exibe mensagem de opção inválida e retorna ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''

    print('Opção inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    os.system('cls')
    main()

def voltar_ao_menu():
    ''' Solicita uma tecla para voltar ao menu principal 
    
    Outputs:
    - Retorna ao menu principal
    '''

    input('\n Digite uma tecla para voltar ao menu principal ')
    main()

def exibir_subtitulo(subtitulo):
    ''' Exibe um subtítulo estilizado na tela 
    
    Inputs:
    - texto: str - O texto do subtítulo
    '''

    os.system('cls')
    linha = '-' * (len(subtitulo) + 4)
    print(linha)
    print(subtitulo)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar novos restaurantes no sistema
    
    Inputs:
    - Nome do restaurante
    - Categoria

    Outputs:

    - Adiciona um novo restaurante a lista de restaurantes
    
    '''

    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu()

    @classmethod
    def listar_restaurantes(cls):
        ''' Lista os restaurantes presentes na lista 
        
        Outputs:
        - Exibe a lista de restaurantes na tela
        '''

        exibir_subtitulo('Listando restaurantes')

        print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}')
        for restaurante in cls.restaurantes:
            nome_restaurante = restaurante._nome
            categoria = restaurante._categoria

            ativo = 'ativado' if restaurante._ativo else 'desativado'
            print(f'- {nome_restaurante.ljust(22)} | {categoria.ljust(20)} | {ativo}')

        voltar_ao_menu()

def alterar_estado_restaurante():
    ''' Altera o estado ativo/desativado de um restaurante 
    
    Outputs:
    - Exibe mensagem indicando o sucesso da operação
    '''

    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
            
    voltar_ao_menu()

def escolher_opcoes():
    ''' Solicita e executa a opção escolhida pelo usuário 
    
    Outputs:
    - Executa a opção escolhida pelo usuário
    '''

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case _ if opcao_escolhida == 1:
                print('Cadastrar restaurante')
                cadastrar_novo_restaurante()
            case _ if opcao_escolhida == 2:
                listar_restaurantes()
                print('Listar restaurantes')
            case _ if opcao_escolhida == 3:
                print('Ativar restaurante')
                alterar_estado_restaurante()
            case _ if opcao_escolhida == 4:
                print('Encerrar o programa')
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    ''' Função principal que inicia o programa '''
    
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()