print('Python na Escola de Programação da Alura\n')

nome = 'Julia'
idade = 21
print(f'Meu nome é {nome} e tenho {idade} anos\n') #fstring é a forma de concatenação

print('A','L','U','R','A',sep='\n')

pi = 3.14159
print(f'\nO valor arredondado de pi é: {pi}')

# Aula 09 - Módulo 02


# Exercício 01

numero_escolhido = int(input('Digite um número'))

if numero_escolhido % 2 == 0:
    print(f'O número {numero_escolhido} é par.')
else:
    print(f'O número {numero_escolhido} é ímpar')

# Exercício 02

idade = int(input('Digite a sua idade'))

match idade:
    case _ if 0 < idade <= 12:
        print('Criançã')
    case _ if 13 < idade < 18:
        print('Adolescente')
    case _ if idade >= 18:
        print('Adulto')
    case _:
        print('Valor inválido!')


# Exercício 03

nome_usuario = 'juwuzinha'
senha = 'senha123'

nome_usuario_inserido = input('Digite o nome de usuário')
senha_inserida = input('Digite a senha')

if nome_usuario_inserido == nome_usuario and senha_inserida == senha:
    print('Login bem sucedido!')
else:
    print('Credenciais inválidas.')


# Exercício 04

coordenada_x = int(input('Insira o valor da coordenada X'))
coordenada_y = int(input('Insira o valor da coordenada Y'))

if 0 > coordenada_x and 0 > coordenada_y:
    print('O ponto está no primeiro quadrante.')
elif 0 < coordenada_x and 0 > coordenada_y:
    print('O ponto está no segundo quadrante.')
elif 0 < coordenada_x and 0 < coordenada_y:
    print('O ponto está no terceiro quadrante.')
elif 0 > coordenada_x and 0 < coordenada_y:
    print('O ponto está no quarto quadrante.')
else:
    print('O ponto está sobre um eixo ou na origem.')


# Aula 10 - Módulo 03


# Exercício 01

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Julia', 'Guilherme', 'Anna', 'Leticia']
anos = [2002, 2024]

# Exercício 02

campeoes_LoL = ['Viego', 'Yone', 'Kayn', 'Aatrox']

for campeao in campeoes_LoL:
    print(campeao)

# Exercício 03

soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)


## Exercício 04

for i in range(10, 0, -1):
    print(i)

## Exercício 05

numero_escolhido = int(input('Escolha um número para verificar a tabuada'))

i = 1

print(f'Tabuada do {numero_escolhido} \n')

while i < 11:
    resultado = numero_escolhido * i
    print(f'{numero_escolhido} x {i} = {resultado}')
    i += 1

# ou

numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")



## Curso - Orientação a Objetos

# Módulo 01. Classes


class Musica:
    nome = ''
    artista = ''
    duracao = int

musica1 = Musica()
musica1.nome = 'Temporary'
musica1.artista = '6BLACK'
musica1.duracao = 258

musica2 = Musica()
musica2.nome = 'Espresso'
musica2.artista = 'Sabrina Carpenter'
musica2.duracao = 255

musica3 = Musica()
musica3.nome = 'Saint'
musica3.artista = 'DPR Ian'
musica3.duracao = 259


# Exercícios

# 1. Atribua o valor 'Italiana' ao atributo categoria da instância restaurante_praca da classe Restaurante.

class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

# 2. Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante.

nome_restaurante = restaurante_praca.nome
print(nome_restaurante)

#3. Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo.

def verificar_restaurante_ativo():
    if restaurante_praca.ativo == False:
        print('O restaurante está ativo.')
    else:
        print('O restaurante está inativo.')

print(verificar_restaurante_ativo())

# 4. Acesse o valor do atributo de classe categoria diretamente da classe Restaurante.

categoria = Restaurante.categoria

# 5. Altere o valor do atributo nome para 'Bistrô'.

restaurante_praca.nome = 'Bistrô'

# 6. Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'

# 7. Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

if restaurante_pizza.categoria == 'Fast Food':
    print(f'A categoria do {restaurante_pizza.nome} é Fast Food')
else:
    print(f'A categoria do {restaurante_pizza.nome} NÃO é Fast Food')

# 8. Mude o estado da instância restaurante_pizza para ativo.

restaurante_pizza.ativo = True

# 9. Imprima no console o nome e a categoria da instância restaurante_praca.

print(f'Nome do restaurante: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')