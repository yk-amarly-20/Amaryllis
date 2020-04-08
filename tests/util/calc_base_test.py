# calc_base.pyのテストケース

import sys
sys.path.append('./../../')
from Amaryllis.util.calc_base import *
import numpy as np


POPULATION = np.array([1188, 774, 487, 295, 172, 96, 51, 26, 13, 6, 2, 1])
DEAD_POPULATION = np.array([414, 287, 192, 123, 76, 45, 25, 13, 7, 3, 1, 1])
I = 0.03
LIFESPAN = 112
X = 100


def test_D():
    D(I, POPULATION[0], X)

    return


def test_N():
    N(I, POPULATION, X, LIFESPAN)

    return


def test_C():
    C(I, DEAD_POPULATION[0], X)

    return


def test_M():
    M(I, DEAD_POPULATION, X, LIFESPAN)

    return


def test_S():
    S(I, POPULATION, X, LIFESPAN)

    return


def test_R():
    R(I, DEAD_POPULATION, X, LIFESPAN)

    return


def test_C_continuous():
    C_continuous(I, DEAD_POPULATION[0], LIFESPAN)

    return


def test_M_continuous():
    M_continuous(I, DEAD_POPULATION, X, LIFESPAN)

    return


if __name__ == '__main__':
    test_D()
    test_N()
    test_C()
    test_M()
    test_S()
    test_R()
    test_C_continuous()
    test_M_continuous()
