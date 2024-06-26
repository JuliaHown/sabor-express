class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_applebee = Restaurante()
restaurante_applebee.nome = 'Applebee'
restaurante_applebee.categoria = 'Gourmet'

restaurante_outback = Restaurante()

restaurantes = [restaurante_applebee, restaurante_outback]

print(vars(restaurante_applebee)) #vars -> dicionário dos atributos e métodos