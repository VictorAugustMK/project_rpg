from lista import pericias as ps
from loguru import logger
import pandas as pd


class ficha:

    def selects(self):
        select_lvl = (input('Nivel desejado: '))

        pericias = pd.DataFrame(ps, copy=False)
        select_peri = (input(f'Seleciona uma periacia: {pericias}'))

        print(f'Nivel: {select_lvl} \n'
              f'Pericias: {select_peri}')


if __name__ == "__main__":
    query = ficha()
    query.selects()
