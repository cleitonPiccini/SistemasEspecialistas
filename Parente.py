from Base import Base


class Parente(Base):
    def __init__(self):
        super().__init__('db.txt')
        self.resultado = ['filho', 'irmão', 'primo', 'tio', 'sobrinho', 'pai', 'avô', 'neto', 'filha', 'irmã', 'prima',
                          'tia', 'sobrinha', 'mãe', 'avó', 'neta']


"""
O seu parente é homem?								homem
O seu parente é mais velho que você?				maisvelho
O seu personagem é filho(a) do seu avô ou avó?		filhoavoa
O seu personagem e você são filhos da mesma mãe?	filhosmesmamae
O seu personagem é filho(a) de sua tia ou tio?		filhotioa
O seu personagem é filho(a) de sua avó ou avô?		filhotioa
O seu personagem amamentou você?					amamentouvoce
"""
