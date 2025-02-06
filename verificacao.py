import frase
import inversao

class Verificacao:

    def __init__(self, instancia_frase, instancia_inversao):
        self.frase_instancia = instancia_frase
        self.inversao_instancia = instancia_inversao

    def verificacao_de_frase(self):
        frase_original = self.frase_instancia.get_frase()
        frase_invertida = self.inversao_instancia.get_frase_invertida()

        if frase_original == frase_invertida:
            print(f"A frase '{frase_original}' é um palíndromo!")
        else:
            print(f"A frase '{frase_original}' não é um palíndromo.")