from lista import pericias as ps
from loguru import logger
import pandas as pd


class ficha:

    def lvl(self):
        select_lvl = (input('Nivel desejado: '))

    def pericia(self):
        pericias = pd.DataFrame(ps, copy=False)
        select_peri = (input(f'Seleciona uma periacia: {pericias}'))
        logger.info(f'Pericia seleciona: {select_peri}')


if __name__ == "__main__":
    query = ficha()
    query.lvl()
    query.pericia()
