from models.avaliacao import Avaliacao
from models.cardapio.item_cardapio import ItemCardapio


class Restaurante:

    restaurantes = []

    # Método Construtor
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self) #Todo objeto criado vai ser inserido na lista

    # Método para exibir o objeto em formato de texto
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    # Método da classe criado para listar
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    # Verifica o status do restaurante
    @property
    def ativo(self):
        return 'Ativo ✅' if self._ativo else 'Não ativo❌'
    
    # Método para alterar o status do restaurante
    def alterar_status(self):
        self._ativo = not self._ativo
    
    # Método para adicionar uma avaliação ao restaurante
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    # Método para calcular a media de avaliações do restaurante
    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    # Método para adicionar itens ao cardapio do restaurante
    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    # Método para exibir os itens do cardápio
    @property
    def exibir_cardapio(self):
        print(f'Cardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item,'descricao'): #hasattr --> se tiver o atributo
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R$ {item._preco} | Tamanho: {item.tamanho}'
                print(mensagem_bebida)


