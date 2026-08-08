"""
jogo.py — O programa principal. RODE ESTE ARQUIVO:  python jogo.py
=====================================================
Isto já vem quase pronto: junta tudo, mostra o menu e roda o jogo.
Sua ÚNICA missão neste arquivo está na função ler_opcao() -> use try/except!
"""

from pet import Pet
import armazenamento


def ler_opcao():
    """Lê a opção do menu digitada pelo usuário."""
    try:
        opcao = int(input("Escolha uma opção: "))

        if 0 <= opcao <= 9:
            return opcao

        print("Erro: a opção deve estar entre 0 e 9.")
        return None

    except ValueError:
        print("Erro: digite um número inteiro.")
        return None

def menu():
    print("\nO que você quer fazer?")
    print("  1 - Alimentar        5 - Dar remédio")
    print("  2 - Brincar          6 - Dar banho")
    print("  3 - Dormir           7 - Trocar de bichinho")
    print("  4 - Ver status       8 - Adotar novo bichinho")
    print("  9 - Salvar jogo      0 - Sair")


def main():
    print("🐣 Bem-vindo ao Bichinho Virtual! 🐣")

def adotar():
    print("Vamos adotar um companheiro! 🐵")
    print("Como devemos chamar seu companheiro?")
    nome = input()
    print("Você adotou seu companheiro!")
    return Pet(nome)



if __name__ == "__main__":

    lista_tamagochi = armazenamento.carregar()
    
    print(lista_tamagochi)
    main()
    if lista_tamagochi == None:
        novo_pet = adotar()
        lista_tamagochi.append(novo_pet)    

    while True:
        menu()
        if ler_opcao() == 1:
            pet.alimentar()
        elif ler_opcao() == 2:
            pet.brincar()
        elif ler_opcao() == 3:
            pet.dormir()
        elif ler_opcao() == 4:
            pet.status
        elif ler_opcao() == 5:
            pet.dar_remedio
        elif ler_opcao() == 6:
            pet.dar_banho
        elif ler_opcao() == 7:
            pet.    
        

        

            

            
