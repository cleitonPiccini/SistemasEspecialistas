import sqlite3
from pathlib import Path


class Database:

    def _cursor(self):
        root = Path(__file__).parent
        self._conn = sqlite3.connect(f'{root}/knowledge.sqlite')
        return self._conn.cursor()

    def _commit(self):
        self._conn.commit()

    def _close(self):
        self._conn.close()

    def get(self, table):
        cursor = self._cursor()
        cursor.execute(f'select sintoma, estado from {table}')
        resultado = cursor.fetchall()
        self._close()
        return resultado
