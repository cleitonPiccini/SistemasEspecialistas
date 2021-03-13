from itertools import filterfalse


class Base:
    def __init__(self, db_path):
        self.resultado = []
        self.db = []
        linhas = open(db_path, 'r').readlines()
        for linha in linhas:
            self.db.append(linha.replace('\n', '').split('-'))
        print(self.db)

    # imprime a quantidade de resultados cadastrados
    def tamanho(self):
        print(len(self.resultado))

    # imprime a probabilidade de acertar o item
    def probabilidade(self):
        num = len(self.resultado)
        if num == 0:
            num = 1
        return int((1 / num) * 100)

    # verifica se o item tem o atributo
    def busca(self, item, atributo):
        for i in range(len(self.db)):
            if item == self.db[i][1]:
                if self.db[i][0] == atributo:
                    return True
        return False

    # remove os resultados que não tem o atributo passado por parametro
    def exclui_sem_atributo(self, atributo):
        if len(self.resultado):
            resultado = filterfalse(lambda x: not self.busca(x, atributo), self.resultado)
            self.resultado = list(resultado)

    # remove os resultados que tem o atributo passado por parametro
    def exclui_com_atributo(self, atributo):
        if len(self.resultado):
            resultado = filterfalse(lambda x: self.busca(x, atributo), self.resultado)
            self.resultado = list(resultado)

    def pergunta(self, pergunta, caract):
        resp = input(pergunta + ': ').upper()
        if resp == 'S':
            self.exclui_sem_atributo(caract)
        elif resp == 'N':
            self.exclui_com_atributo(caract)
