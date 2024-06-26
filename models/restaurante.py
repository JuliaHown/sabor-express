class Restaurante:

    restaurantes = []

    # Método Construtor
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self) #Todo objeto criado vai ser inserido na lista

    # Método para exibir o objeto em formato de texto
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    # Método criado para listar
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_applebee = Restaurante('Applebee','Gourmet')
restaurante_outback = Restaurante('Australiana','Steakhouse')

Restaurante.listar_restaurantes()