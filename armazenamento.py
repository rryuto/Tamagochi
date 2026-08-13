"""
armazenamento.py — Salvar e carregar o bichinho em um arquivo JSON.
=====================================================
DESAFIO BÔNUS! Aqui o try/except brilha, porque ler arquivo pode dar erro.
Enquanto você não implementar, o jogo funciona normal (só não salva).
"""

import json
from pet import Pet as p

ARQUIVO = "save_bichinhos.json"


def pet_de_dict(dados):
    """Recria um Pet a partir de um dicionário (o contrário de para_dict)."""
    # TODO (bônus): use os dados pra criar e devolver um Pet.
    # 🔧 [CLINE] try/except adicionado: protege contra JSON malformado
    #            (faltando chaves como "nome", "fome", etc.)
    try:
        if dados is None:
            return None
        lista_pets = []
        for d in dados:
            lista_pets.append(p(**d))
        return lista_pets
    except (TypeError, KeyError):
        print("Erro: dados de save inválidos ou corrompidos.")
        return None
    pass


def salvar(pets):
    # TODO (bônus): transforme cada bichinho em dicionário (para_dict())
    pet_save = []
    for i in range(0, len(pets)):
        pet_save.append(pets[i].para_dict())

    # 🔧 [CLINE] try/except adicionado: protege contra falhas de escrita
    #            (disco cheio, permissão negada, arquivo em uso...)
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            json.dump(pet_save, f, ensure_ascii=False, indent=4)
        print("💾 Jogo salvo com sucesso!")
    except OSError as e:
        print(f"Erro ao salvar o jogo: {e}")


def carregar():
    """Deve devolver a lista de bichinhos salvos, ou None se não houver save."""
    # TODO (bônus): leia o arquivo JSON e recrie os bichinhos.
    # 🔧 [CLINE] try/except adicionado: protege contra arquivo inexistente
    #            (FileNotFoundError) e arquivo corrompido (JSONDecodeError)
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Nenhum save encontrado. Começando do zero!")
        return None
    except json.JSONDecodeError:
        print("Arquivo de save corrompido. Começando do zero!")
        return None

    return None