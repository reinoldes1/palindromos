import frase

class Inversao:
    
    def __init__(self, instancia_frase):
        self.frase_instancia = instancia_frase
        self.frase_invertida = ""

    def inverter_frase(self):
        frase = self.frase_instancia.get_frase()
        self.frase_invertida = frase[::-1]  
        print(f"Sua frase invertida é: {self.frase_invertida}")

    def get_frase_invertida(self):
        return self.frase_invertida


