import sys
import pandas as pd

from expertise import pericias as exp, tendencias as td
from loguru import logger


class Token:

    def user_and_race(self):

        try:
            insert_player = input('Nome do Jogador: ')
            insert_char = input('Nome do Personagem: ')

            ok = False
            trend = ''
            while True:

                moral = pd.DataFrame(td, copy=False)
                insert_trend = input(f'Tendencia:{moral}\n')
                if insert_trend in td:
                    ok = True
                else:
                    print('\033[0;31mERRO! Digite alguma das tendências acima.\033[m')
                if ok:
                    break
            return trend
        except Exception:
            logger.exception('Error!')
    def selects_lvl(self):

        try:

            num = False
            lvl = 0
            while True:
                select_lvl = (input('Nivel desejado:'))
                if select_lvl.isnumeric():
                    lvl = int(select_lvl)
                    num = True
                else:
                    print('\033[0;31mERRO! Digite apenas números.\033[m')
                if num:
                    break
            return lvl

        except Exception:
            logger.exception('Error - Insert a level!')

    def select_expertise(self):

        try:

            expert = False
            skill = ''
            while True:
                expertise = pd.DataFrame(exp, copy=False)
                select_expert = (input(f'Seleciona uma das periacia: {expertise}\n'))

                if select_expert in exp:
                    skill = select_expert
                    expert = True
                else:
                    print('\033[0;31mERRO! Digite alguma pericia acima.\033[m')
                if expert:
                    break
            return skill

        except Exception:
            logger.exception('Error - Insert a expertise!')


if __name__ == "__main__":

    token = Token()

    token.user_and_race()
    token.selects_lvl()
    token.select_expertise()
