class Perguntas:
    def __init__(self):
        self.level = [
            ['Seu Pet está agitado?', 'agitado'],
            ['O seu Pet está comendo bem?', 'alimentado'],
            ['O ambiente é adequado?', 'ambiente_adequado'],
            ['O seu Pet fez atividade física?', 'se_movimenta'],
        ]

    def proxima(self):
        pergunta = self.level[0]
        del self.level[0]
        return pergunta
