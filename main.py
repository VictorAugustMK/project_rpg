import sys
import pandas as pd

from expertise import pericias as exp
from loguru import logger


class ficha:

    def selects_lvl(self):

        ok = False
        lvl = 0
        while True:
            select_lvl = (input('Nivel desejado: '))
            if select_lvl.isnumeric():
                lvl = int(select_lvl)
                ok = True
            else:
                print('\033[0;31mERRO! Digite apenas números.\033[m')
            if ok:
                break
        return lvl

    def select_expertise(self):

        expert = False
        skill = ''
        while True:
            expertise = pd.DataFrame(exp, copy=False)
            select_expert = (input(f'Seleciona uma periacia: {expertise}'))

            if select_expert in exp:
                skill = select_expert
                expert = True
            else:
                print('\033[0;31mERRO! Digite alguma pericia acima.\033[m')
            if expert:
                break
        return skill

if __name__ == "__main__":
    query = ficha()

    query.selects_lvl()
    query.select_expertise()
