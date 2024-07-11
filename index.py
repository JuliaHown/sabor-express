from models.restaurante import Restaurante

restaurante_outback = Restaurante('outblack','Steakhouse')

restaurante_outback.alterar_status()
restaurante_outback.receber_avaliacao('Julia', 10)
restaurante_outback.receber_avaliacao('Jhulia', 5)
restaurante_outback.receber_avaliacao('Guilherme', 4)
restaurante_outback.receber_avaliacao('Leticia', 3)
restaurante_outback.receber_avaliacao('Anna', 4)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()