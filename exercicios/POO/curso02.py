## Curso - Orientação a Objetos

# Módulo 01. Classes


class Musica:

    musicas = []

    nome = ''
    artista = ''
    duracao = int

    def __init__(self, artista, duracao = 0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'

musica1 = Musica('Temporary', '6BLACK', 258)
musica2 = Musica('Espresso', 'Sabrina Carpenter', 255)
musica3 = Musica('Saint', 'DPR Ian', 259)

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



# Módulo 02 - Constrtutor
# Exercícios


# 1.
class Carro:
    modelo = ''
    cor = ''
    ano = int

    def __init__(self, modelo, cor, ano = 0):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro('Lamborghini Huracan', 'Cinza metálico', 2024)

# 2. 3. e 4.
class Restaurante:

    restaurantes = []

    nome = ''
    categoria = ''
    ativo = False
    avaliacao = int
    ano = int

    def __init__(self, nome, categoria, ativo, avaliacao = 0, ano = 0):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.avaliacao = avaliacao
        self.ano = ano
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo} | {self.avaliacao} | {self.ano}'

restaurante = Restaurante('Espaço Kazu', 'Japonês', 'Ativo', 4, 2024)
print(restaurante)

# 5. 
class Cliente:
    def __init__(self, nome = '', telefone = 0, email = '', senha = ''):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha

cliente1 = Cliente('Akali', '99999-9999', 'akali@gmail.com', 'senha123')
cliente2 = Cliente('Yasuo', '99999-9999', 'yasuo@gmail.com', 'senha321')
cliente3 = Cliente('Ahri', '99999-9999', 'ahri@gmail.com', 'senha231')
