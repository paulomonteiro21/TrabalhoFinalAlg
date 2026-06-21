# Função que limpa o terminal. OBS: peguei da internet
def limpar():
    print('\033[H\033[J', end='')

def operação_sucesso():
    print('\n✅ Operação feita com sucesso!')
    input('\nPressione ENTER para continuar...')
# Exibe mensagem de livro não encontrado
def naoencontrado(x):
    print(f'\n❌ "{x}" não encontrado')
    input('\nPressione ENTER para continuar...')


class Livros:
    titulo = ''
    autor = ''
    ano = 0
    codigo = ''
    status = ''


# Função para printar os dados dos livros
def print_livros(livros,i):
    print('-' * 40)

    print(f'Título: {livros[i].titulo}')
    print(f'Autor: {livros[i].autor}')
    print(f'ano: {livros[i].ano}')
    print(f'Código: {livros[i].codigo}')
    print(f'Status: {livros[i].status}')

    print('-' * 40)


# Percorre a lista de livros e retorna o índice do livro com o código informado, ou -1 se não encontrar
def pega_codigo(livros,codigo): 
	for i in range(len(livros)):
		if livros[i].codigo == codigo:
			return i
	return -1


# Bubble sort que ordena alfabeticamente, .lower para garantir que maiúsculas e minúsculas não interfiram na ordenação
def ordenar_livros(livros):
    for i in range(len(livros)):
        for j in range(0, len(livros)-i-1):
            if livros[j].titulo.lower() > livros[j+1].titulo.lower():
                livros[j], livros[j+1] = livros[j+1], livros[j]


# Cadastra um novo livro na lista, verificando se o código já existe
def cadastrar_livro(livros):
    limpar()
    print('=' * 40)
    print('         CADASTRAR LIVRO')
    print('=' * 40)

    livro = Livros()
    livro.titulo = input('Título: ')
    livro.autor = input('Autor: ')
    livro.ano = int(input('Ano: '))
    livro.codigo = input('Código: ')
    i = pega_codigo(livros,livro.codigo)
    if i!=-1:
        print('\n❌ Esse livro já está no sistema')
        input('\nPressione ENTER para continuar...')
        return
    livro.status = 'Disponível'
    livros.append(livro)

    operação_sucesso()


# Consulta um livro por código ou por autor
def consultar_livros(livros):
    limpar()
    print('=' * 40)
    print('         CONSULTAR LIVROS')
    print('=' * 40)

    opc = int(input('1 - Por código\n2 - Por autor\nOpção: '))
    if opc == 1:
        codigo = input('Digite o código do livro que deseja consultar: ')
        i = pega_codigo(livros,codigo)
        if i!=-1:
            print_livros(livros,i)
            operação_sucesso()
        else:
            naoencontrado(codigo)
    else:
        autor = input('Autor: ')
        encontrou = False
        for i in range(len(livros)):
            if autor == livros[i].autor:
               print_livros(livros,i)
               encontrou = True
        if encontrou:
            operação_sucesso()
        else:
            naoencontrado(autor)


# Altera os dados de um livro existente
def alterar_livro(livros):
    limpar()
    print('=' * 40)
    print('         ALTERAR LIVRO')
    print('=' * 40)

    codigo = input('Código do livro: ')
    i = pega_codigo(livros,codigo)
    if i!=-1:
        print('\nDigite os NOVOS DADOS:')
        livros[i].titulo = input('Digite o TÍTULO do livro: ')
        livros[i].autor = input('Digite o AUTOR do livro: ')
        livros[i].ano = int(input('Digite o ANO de publicação do livro: '))
        
        operação_sucesso()
    else:
        naoencontrado(codigo)


# Remove um livro da lista pelo código
def remover_livro(livros):
    limpar()
    print('=' * 40)
    print('         REMOVER LIVRO')
    print('=' * 40)

    codigo = input('Código do livro: ')
    i=pega_codigo(livros,codigo)
    if i !=-1:
        certeza = input('Tem certeza? (s/n)')
        if certeza == 's':
            livros.pop(i)
            operação_sucesso()
        else:
            print('\nRemoção cancelada')
            input('\nPressione ENTER para continuar...')
    else:
        naoencontrado(codigo)


# Lista todos os livros ordenados alfabeticamente
def listar_livros(livros):
    limpar()
    print('=' * 40)
    print('         LISTA DE LIVROS')
    print('=' * 40)

    ordenar_livros(livros)
    print(f'Livros: {len(livros)}')
    for i in range(len(livros)):
        print(f'{livros[i].titulo}, {livros[i].ano}')
   
    print('=' * 40)
    input('\nPressione ENTER para continuar...')


# Empresta um livro, verificando se já está emprestado e marcando como Indisponível
def emprestar_livro(livros, livros_emprestados):
    limpar()
    print('=' * 40)
    print('         EMPRESTAR LIVRO')
    print('=' * 40)

    codigo = input('CÓDIGO: ')
    i2=pega_codigo(livros_emprestados,codigo)
    if i2!=-1:
        print('\n❌ Livro já emprestado')
        input('\nPressione ENTER para continuar...')
        return
    
    i=pega_codigo(livros,codigo)
    if i!=-1:
        livros_emprestados.append(livros[i])
        livros[i].status = 'Indisponível'
        operação_sucesso()
    else:
        naoencontrado(codigo)

# Devolve um livro, removendo da lista de emprestados e marcando como Disponível
def devolver_livro(livros_emprestados):
    limpar()
    print('=' * 40)
    print('         DEVOLVER LIVRO')
    print('=' * 40)
    codigo = input('CÓDIGO: ')
    i=pega_codigo(livros_emprestados,codigo)
    if i!=-1:
        livros_emprestados[i].status = 'Disponível'  
        livros_emprestados.pop(i)
        
        operação_sucesso()
    else:
        naoencontrado(codigo)


# Função principal que exibe o menu e chama as funções correspondentes
def menu():
    op = 0
    livros = []
    livros_emprestados = []
    while True:
        limpar()
        print('=' * 40)
        print('       SISTEMA DE BIBLIOTECA')
        print('=' * 40)
        print('  1 - Cadastrar livro')
        print('  2 - Consultar livros')
        print('  3 - Alterar livros')
        print('  4 - Remover livros')
        print('  5 - Listar livros')
        print('  6 - Emprestar livro')
        print('  7 - Devolver livro')
        print('  8 - Sair')
        print('=' * 40)
        op = int(input('  Opção: '))
        if op == 1:
            cadastrar_livro(livros)
        if op == 2:
            consultar_livros(livros)
        if op == 3:
             alterar_livro(livros)
        if op == 4:
             remover_livro(livros)
        if op == 5:
             listar_livros(livros)
        if op == 6:
             emprestar_livro(livros, livros_emprestados)
        if op == 7:
             devolver_livro(livros_emprestados)
        if op == 8:
            limpar()
            print('=' * 40)
            print('        Até logo!')
            print('=' * 40)
            break