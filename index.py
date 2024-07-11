from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

restaurante_gendai = Restaurante('gendai','culinária japonesa')

bebida_suco = Bebida('Suco de Laranja', 10.00, 'Grande')
prato_domburi = Prato('Chicken Domburi', 30.90, 'O melhor domburi de frango de SP')

restaurante_gendai.adicionar_no_cardapio(bebida_suco)
restaurante_gendai.adicionar_no_cardapio(prato_domburi)

def main():
    restaurante_gendai.exibir_cardapio

if __name__ == '__main__':
    main()