import frase
import inversao
import verificacao


class Palindromo:

    @staticmethod
    def palindromo():
        while True: 
            print("Vamos verificar esses palindromos ai meu mano")
            
            instancia_frase = frase.Frase()
            instancia_frase.pegar_frase()

            instancia_inversao = inversao.Inversao(instancia_frase)
            instancia_verificacao = verificacao.Verificacao(instancia_frase, instancia_inversao)

            instancia_inversao.inverter_frase()
            instancia_verificacao.verificacao_de_frase()
        
            continuar = input("Você deseja continuar verificando os palindromos? (s/n): ").strip().lower()
            if continuar != 's':
                print("Saindo do programa...")
                break

Palindromo.palindromo()