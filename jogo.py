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
    # Sua tarefa: proteger com try/except. Se der erro, avise e devolva None.
  
    return int(input("Escolha uma opção: "))   

def menu():
    print("\nO que você quer fazer?")
    print("  1 - Alimentar        5 - Dar remédio")
    print("  2 - Brincar          6 - Dar banho")
    print("  3 - Dormir           7 - Trocar de bichinho")
    print("  4 - Ver status       8 - Adotar novo bichinho")
    print("  9 - Salvar jogo      0 - Sair")


def main():
    print("🐣 Bem-vindo ao Bichinho Virtual! 🐣")

    


if __name__ == "__main__":
    main()
