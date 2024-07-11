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
    
    # Método da classe criado para listar
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    # Método para alterar o status do restaurante
    def alterar_status(self):
        self._ativo = not self._ativo

    # Verifica o status do restaurante
    @property
    def ativo(self):
        return 'Ativo ✅' if self._ativo else 'Não ativo❌'

