from models.restaurante import Restaurante

restaurante_applebee = Restaurante('applebee','Gourmet')
restaurante_outback = Restaurante('outblack','Steakhouse')

restaurante_applebee.alterar_status()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()