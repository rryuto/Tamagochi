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
    pet = p(**dados)
    return pet
    pass


def salvar(pets):
    # TODO (bônus): transforme cada bichinho em dicionário (para_dict())
    pet_save = p.para_dict(pets)
    with open(ARQUIVO, "w", encoding="utf=8") as f:
        json.dump(pet_save, f, ensure_ascii=False, indent=4)
    print(f"💾")


def carregar():
    """Deve devolver a lista de bichinhos salvos, ou None se não houver save."""
    # TODO (bônus): leia o arquivo JSON e recrie os bichinhos.
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

    return None
