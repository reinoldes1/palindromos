class Frase:

    def __init__(self):
        self.frase_usuario = ""
        self.tamanho = 0

    def pegar_frase(self):
        self.frase_usuario = input ("Digite uma frase: ").replace(" ", "").lower()
        self.tamanho = len(self.frase_usuario)
        print(f"Sua frase é {self.frase_usuario} e tem o tamanho de {self.tamanho} letras")

    def get_frase(self):
        return self.frase_usuario
    
    def get_tamanho(self):
        return self.tamanho