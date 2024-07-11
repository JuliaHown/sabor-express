from models.restaurante import Restaurante

restaurante_outback = Restaurante('outblack','Steakhouse')

restaurante_outback.alterar_status()

restaurante_outback.receber_avaliacao('Julia', 9)
restaurante_outback.receber_avaliacao('Guilherme', 8)
restaurante_outback.receber_avaliacao('Leticia', 7)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()