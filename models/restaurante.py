class Restaurante:

    restaurantes = []

    # Método Construtor
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self) #Todo objeto criado vai ser inserido na lista

    # Método para exibir o objeto em formato de texto
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    # Método criado para listar
    def listar_restaurantes():
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    # Verifica o status do restaurante
    @property
    def ativo(self):
        return 'Ativo ✅' if self._ativo else 'Não ativo❌'

restaurante_applebee = Restaurante('applebee','Gourmet')
restaurante_outback = Restaurante('outblack','Steakhouse')

Restaurante.listar_restaurantes()