class Livros:
    titulo = ''
    autor = ''
    Ano = 0
    codigo = ''
    status = ''

def pega_codigo(livros,codigo): 
	for i in range(len(livros)):
		if livros[i].codigo == codigo:
			return i
	return -1

def cadastrar_livro(livros):
    livro = Livros()
    '''livro.titulo = input('Digite o título do livro: ')'''
    livro.autor = input('Digite o autor do livro: ')
    '''livro.Ano = int(input('Digite o ano de publicação do livro: '))'''
    livro.codigo = input('Digite o código do livro: ')
    i = pega_codigo(livros,livro.codigo)
    if i!=-1:
        print('Esse livro já está no sistema')
        return
    livro.status = 'Disponível'
    livros.append(livro)
    return livros

def consultar_livros(livros):
    opc = int(input('Digite 1 para consultar por código ou 2 para consultar por autor: '))
    if opc == 1:
        codigo = input('Digite o código do livro que deseja consultar: ')
        i = pega_codigo(livros,codigo)
        if i!=-1:
           print_livros(livros,i)
        else:
            print(f'Livro não encontrado.')
    else:
        autor = input('Digite o nome do autor: ')
        for i in range(len(livros)):
            if autor == livros[i].autor:
               print_livros(livros,i)

def print_livros(livros,i):
        '''print(f'Título: {livros[i].titulo}')'''
        print(f'Autor: {livros[i].autor}')
        '''print(f'Ano: {livros[i].Ano}')'''
        print(f'Código: {livros[i].codigo}')
        '''print(f'Status: {livros[i].status}')''' 

def alterar_livro(livros):
     codigo = input('Digite o Código do livro que você deseja alterar: ')
     i = pega_codigo(livros,codigo)
     if i!=-1:
        print(f'Digite os NOVOS DADOS:')
        '''livro[i].titulo = input('Digite o título do livro: ')'''
        livros[i].autor = input('Digite o autor do livro: ')
        '''livro[i].Ano = int(input('Digite o ano de publicação do livro: '))'''
        livros[i].codigo = input('Digite o código do livro: ')
        print(f'Livro alterado com sucesso!')
     else:
          print(f'Livro não encontrado')

def main():
    op = 0
    livros = []
    while True:
        print(f'1 - Cadastrar livro')
        print(f'2 - Consultar livros')
        print(f'3 - Alterar livros')
        print(f'0 - Sair')
        op = int(input(f'Digite a opção desejada: '))
        if op == 1:
            cadastrar_livro(livros)
        if op == 2:
            consultar_livros(livros)
        if op == 3:
             alterar_livro(livros)
        if op == 0:
            break

main()