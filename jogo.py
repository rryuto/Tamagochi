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
    # 🔧 [CLINE] try/except estendido: captura EOFError também
    #            (quando o usuário fecha o terminal durante o input)
    try:
        opcao = int(input("Escolha uma opção: "))

        if 0 <= opcao <= 9:
            return opcao

        print("Erro: a opção deve estar entre 0 e 9.")
        return None

    except ValueError:
        print("Erro: digite um número inteiro.")
        return None
    except EOFError:
        print("Entrada encerrada. Saindo...")
        return 0

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

    # 🔧 [CLINE] try/except adicionado: protege contra EOFError
    #            (entrada encerrada de forma inesperada) e nome vazio
    try:
        nome = input()
    except EOFError:
        nome = "SemNome"
    
    if nome.strip() == "":
        print("Nome vazio! Vou chamá-lo de SemNome.")
        nome = "SemNome"

    print("Você adotou seu companheiro!")
    return Pet(nome)

if __name__ == "__main__":

    # 🔧 [CLINE] try/except adicionado: protege contra IndexError
    #            caso a lista de bichinhos venha vazia
    try:
        dados = armazenamento.carregar()
    except Exception as e:
        print(f"Erro inesperado ao carregar: {e}")
        dados = None

    if dados is None or len(dados) == 0:
        novo_pet = adotar()
        lista_tamagochi = [novo_pet]
    else:
        lista_tamagochi = armazenamento.pet_de_dict(dados)
        # 🔧 [CLINE] Se pet_de_dict retornar None (dados corrompidos),
        #            criamos um pet novo para o jogo não quebrar
        if lista_tamagochi is None or len(lista_tamagochi) == 0:
            print("Recuperação automática: adotando um novo bichinho!")
            novo_pet = adotar()
            lista_tamagochi = [novo_pet]

    cont_pet = 0
    try:
        print(f"🐵{lista_tamagochi[cont_pet].nome} foi invocado!")
    except (IndexError, AttributeError):
        print("Nenhum bichinho disponível. Adote um primeiro!")
        novo_pet = adotar()
        lista_tamagochi = [novo_pet]

    main()
    while lista_tamagochi[cont_pet].vivo:
        menu()
        opcao = ler_opcao()
        # 🔧 [CLINE] try/except adicionado: se a ação quebrar
        #            (ex: atributos inválidos de um save corrompido),
        #            o jogo mostra o erro mas não fecha
        try:
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
        except Exception as e:
            print(f"Erro inesperado: {e}")
            print("Tente outra ação.")