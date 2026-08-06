"""
pet.py — A classe do seu bichinho virtual.
=====================================================
Aqui fica TODO o comportamento do bichinho (atributos + métodos).
Procure os  # TODO  e complete! O método alimentar() já está pronto
como EXEMPLO pra você ver o padrão. Siga a mesma ideia nos outros.
"""

import random


class Pet:
    def __init__(self, nome, fome=50, felicidade=50, energia=50, vivo=True):
        self.nome = nome
        self.fome = fome              # 0 = cheio   | 100 = faminto
        self.felicidade = felicidade  # 0 = triste  | 100 = radiante
        self.energia = energia        # 0 = exausto | 100 = com pique
        self.vivo = vivo
        # TODO (bônus): crie mais atributos aqui! Ex:
        #   self.saude = 100
        #   self.higiene = 50
        #   self.rodadas = 0
        #   self.pontos = 0

    # ==================== AÇÕES ====================

    def alimentar(self):
        """✅ EXEMPLO PRONTO — use como modelo pros outros métodos."""
        self.fome = max(0, self.fome - 30)   # max(0, ...) não deixa passar de 0
        print(f"🍎 Você alimentou {self.nome}. Que delícia!")

    def brincar(self):
        # TODO: brincar deve AUMENTAR a felicidade e GASTAR energia.

        pass

    def dormir(self):
        # TODO: dormir deve RECUPERAR energia.

        pass

    # --- Ações bônus: o menu já chama estas, agora é implementar! ---

    def dar_banho(self):
        # TODO (bônus): crie um atributo self.higiene no __init__ e aumente aqui.
        print("🛁 (Dar banho ainda não foi implementado.)")

    def dar_remedio(self):
        # TODO (bônus): crie um atributo self.saude no __init__ e aumente aqui.
        print("💊 (Dar remédio ainda não foi implementado.)")

    # ==================== PASSAGEM DO TEMPO ====================

    def passar_tempo(self):
        """Chamado depois de cada ação. O tempo não perdoa: tudo piora sozinho!"""
        # TODO: faça a fome SUBIR e a felicidade/energia CAÍREM um pouco.
        pass

    def verificar_saude(self):
        # TODO: se a fome chegar a 100 OU a felicidade chegar a 0,
        pass

    # ==================== VISUAL (já vem pronto o básico) ====================

    def barra(self, valor):
        """Desenha uma barrinha de 0 a 100. (pode melhorar depois!)"""
        cheios = valor // 10
        return "#" * cheios + "-" * (10 - cheios) + f" {valor}"

    def status(self):
        """Mostra a situação do bichinho. Você pode deixar mais bonito!"""
        print("\n" + "=" * 34)
        print(f"  {self.nome}")
        print("-" * 34)
        print(f"  Fome......: {self.barra(self.fome)}")
        print(f"  Felicidade: {self.barra(self.felicidade)}")
        print(f"  Energia...: {self.barra(self.energia)}")
        print("=" * 34)
        # TODO (bônus): mostre um rostinho que muda com o humor,
        #               e as barras dos novos atributos (saúde, higiene...).

    # ==================== SALVAR EM JSON (desafio bônus) ====================

    def para_dict(self):
        """Transforma o bichinho num dicionário, pra virar JSON depois."""
        # TODO (bônus): devolva um dicionário com os atributos do bichinho.
        pass
