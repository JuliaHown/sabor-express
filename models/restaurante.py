class Restaurante:

    # Método Construtor
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    # Método para exibir o objeto em formato de texto
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_applebee = Restaurante('Applebee','Gourmet')
restaurante_outback = Restaurante('Australiana','Steakhouse')

restaurantes = [restaurante_applebee, restaurante_outback]

print(restaurante_applebee) 
print(restaurante_outback)