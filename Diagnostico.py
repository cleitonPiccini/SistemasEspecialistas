from Base import Base


class Diagnostico(Base):
    def __init__(self):
        super().__init__('db.txt')
        self.resultado = ['cansado', 'estressado', 'deprimido', 'faminto', 'saudavel']


"""
O seu Pet está agitado?'			->		'agitado'
O seu Pet está comendo bem?'		->		'alimentado'
'O ambiente é adequado?'			->		'ambiente_adequado'
'O seu Pet fez atividade física?' 	-> 		'se_movimenta',		
"""
