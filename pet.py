"""
pet.py — A classe do seu bichinho virtual.
=====================================================
Aqui fica TODO o comportamento do bichinho (atributos + métodos).
Procure os  # TODO  e complete! O método alimentar() já está pronto
como EXEMPLO pra você ver o padrão. Siga a mesma ideia nos outros.
"""

import random


class Pet:
    def __init__(self, nome, fome=50, felicidade=50, energia=50, vivo=True, saude=100, higiene=50, rodadas=0, pontos=0):
        self.nome = nome
        self.fome = fome              # 0 = cheio   | 100 = faminto
        self.felicidade = felicidade  # 0 = triste  | 100 = radiante
        self.energia = energia        # 0 = exausto | 100 = com pique
        self.vivo = vivo
        # TODO (bônus): crie mais atributos aqui! Ex:
        self.saude = saude
        self.higiene = higiene
        self.rodadas = rodadas
        self.pontos = pontos

    # ==================== AÇÕES ====================

    def alimentar(self):
        """✅ EXEMPLO PRONTO — use como modelo pros outros métodos."""
        self.fome = (self.fome - 30)   # max(0, ...) não deixa passar de 0
        self.rodadas += 1
        self.pontos += 10
        self.saude = max(0, self.saude - 10)
        print(f"🍎 Você alimentou {self.nome}. Que delícia!")

    def brincar(self):
        # TODO: brincar deve AUMENTAR a felicidade e GASTAR energia.
        self.felicidade = max(100, self.felicidade + 20)
        self.energia = max(0, self.energia - 10)
        self.higiene = max(0, self.higiene - 20)
        self.saude = max(0, self.saude - 10)
        self.rodadas += 1
        self.pontos += 10
        print(f"Voce brincou com {self.nome}. Uhull!! ☆*: .｡. o(≧▽≦)o .｡.:*☆")
        pass

    def dormir(self):
        # TODO: dormir deve RECUPERAR energia.
        self.energia = max(100, self.energia + 25)
        self.saude = max(0, self.saude - 10)
        self.rodadas += 1
        self.pontos += 10
        print(f"{self.nome} teve um descanso e recuperou suas energias! 🤗")
        pass

    # --- Ações bônus: o menu já chama estas, agora é implementar! ---

    def dar_banho(self):
        # TODO (bônus): crie um atributo self.higiene no __init__ e aumente aqui.
        self.higiene = max(100, self.higiene + 50)
        self.saude = max(0, self.saude - 10)
        self.rodadas += 1
        self.pontos += 10
        print(f"🛁 {self.nome} Tomou um banho e esta rejuvenecido!")

    def dar_remedio(self):
        # TODO (bônus): crie um atributo self.saude no __init__ e aumente aqui.
        self.saude = max(100, self.saude + 25)
        self.rodadas += 1
        self.pontos += 10
        print(f"💊 {self.nome} foi medicado e está mais saudável!")

    # ==================== PASSAGEM DO TEMPO ====================

    def passar_tempo(self):
        """Chamado depois de cada ação. O tempo não perdoa: tudo piora sozinho!"""
        # TODO: faça a fome SUBIR e a felicidade/energia CAÍREM um pouco.
        self.fome = max(0, self.fome + 15)
        self.felicidade = max(0, self.felicidade - 15)
        self.energia = max(0, self.energia -15)
        self.saude = max(0, self.saude - 10)
        self.rodadas += 1
        pass

    def verificar_saude(self):
        # TODO: se a fome chegar a 100 OU a felicidade chegar a 0,
        if self.fome == 100:
            print(f"😿 {self.nome} está com muita fome! hora de alimenta-lo🧀")
        elif self.felicidade == 0:
            print(f"😢💔 {self.nome} está muito triste e solitario, brinque com ele!")
        self.pontos += 10
        if self.saude == 0:
            print(f"💀{self.nome} faleceu.")
            self.vivo = False
        pass

    # ==================== VISUAL (já vem pronto o básico) ====================

    def barra(self, valor):
        """Desenha uma barrinha de 0 a 100. (pode melhorar depois!)"""
        cheios = valor // 10
        return "#" * cheios + "-" * (10 - cheios) + f" {valor}"

    def status(self):
        """Mostra a situação do bichinho. Você pode deixar mais bonito!"""
        print("\n" + "=" * 34)
        if 0 >= self.felicidade >= 25:
            print(f"😿💔  {self.nome}")
        elif 26 >= self.felicidade >= 50:
            print(f"😮‍💨🐾 {self.nome}")
        elif 51 >= self.felicidade >= 75:
            print(f"😊💕 {self.nome}")
        elif 76 >= self.felicidade >= 100:
            print(f"🥰❤️ {self.nome}")
        print("-" * 34)
        print(f"  Fome......: {self.barra(self.fome)}")
        print(f"  Felicidade: {self.barra(self.felicidade)}")
        print(f"  Energia...: {self.barra(self.energia)}")
        print(f"  Saude.....: {self.barra(self.saude)}")
        print(f"  Higiene...: {self.barra(self.higiene)}")
        print(f"Rodada: {self.rodadas}")
        print("=" * 34)
        # TODO (bônus): mostre um rostinho que muda com o humor,
        #               e as barras dos novos atributos (saúde, higiene...).

    # ==================== SALVAR EM JSON (desafio bônus) ====================

    def para_dict(self):
        """Transforma o bichinho num dicionário, pra virar JSON depois."""
        # TODO (bônus): devolva um dicionário com os atributos do bichinho.
        return {
            "nome" : self.nome, 
            "fome" : self.fome,
            "felicidade" : self.felicidade, 
            "energia" : self.energia, 
            "saude" : self.saude,
            "higiene" : self.higiene,
            "vivo" : self.vivo
        }
        pass
