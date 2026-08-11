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

    dados = armazenamento.carregar()

    if dados is None or len(dados) == 0:
        novo_pet = adotar()
        lista_tamagochi = [novo_pet]
    else:
        lista_tamagochi = armazenamento.pet_de_dict(dados)

    cont_pet = 0
    print(f"🐵{lista_tamagochi[cont_pet].nome} foi invocado!")
    main()
    while lista_tamagochi[cont_pet].vivo:
        menu()
        opcao = ler_opcao()
        if opcao == 1:
            lista_tamagochi[cont_pet].alimentar()
            lista_tamagochi[cont_pet].passar_tempo()
            lista_tamagochi[cont_pet].status()
            lista_tamagochi[cont_pet].verificar_saude()
        elif opcao == 2:
            lista_tamagochi[cont_pet].brincar()
            lista_tamagochi[cont_pet].passar_tempo()
            lista_tamagochi[cont_pet].status()
            lista_tamagochi[cont_pet].verificar_saude()
        elif opcao == 3:
            lista_tamagochi[cont_pet].dormir()
            lista_tamagochi[cont_pet].passar_tempo()
            lista_tamagochi[cont_pet].status()
            lista_tamagochi[cont_pet].verificar_saude()
        elif opcao == 4:
            lista_tamagochi[cont_pet].status()
            lista_tamagochi[cont_pet].passar_tempo()
            lista_tamagochi[cont_pet].status()
            lista_tamagochi[cont_pet].verificar_saude()
        elif opcao == 5:
            lista_tamagochi[cont_pet].dar_remedio()
            lista_tamagochi[cont_pet].passar_tempo()
            lista_tamagochi[cont_pet].status()
            lista_tamagochi[cont_pet].verificar_saude()
        elif opcao == 6:
            lista_tamagochi[cont_pet].dar_banho()
            lista_tamagochi[cont_pet].passar_tempo()
            lista_tamagochi[cont_pet].status()
            lista_tamagochi[cont_pet].verificar_saude()
        elif opcao == 7:
            print("\n")
            print("😶‍🌫️")
            if cont_pet < len(lista_tamagochi) - 1:
                cont_pet += 1
                lista_tamagochi[cont_pet]
                print(f"Um {lista_tamagochi[cont_pet].nome} selvagem aparece!")
            else:
                cont_pet = 0
                lista_tamagochi[cont_pet]
                print(f"Um {lista_tamagochi[cont_pet].nome} selvagem aparece!")
        elif opcao == 8:
            novo_pet = adotar()
            lista_tamagochi.append(novo_pet)

        elif opcao == 9:
            armazenamento.salvar(lista_tamagochi)
        elif opcao == 0:
            print("Até a proxima!")
            break
        

            

            
