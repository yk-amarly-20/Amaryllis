# single.pyのテスト

import numpy as np
import sys
sys.path.append('./../../')
from Amaryllis.models.single import *

# テスト用の仮データ
POPULATION = np.array([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])
LIFESPAN = 10
X = 0
I = 0.03
N = 2
F = 1


def test_single_term_insurance():
    print(single_term_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN))
    
    return


def test_single_life_insurance():
    print(single_life_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN))

    return


def test_single_endowment_insurance():
    print(single_endowment_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN))

    return


def test_single_increasing_term_insurance():
    print(single_increasing_term_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN))

    return


def test_single_decreasing_term_insurance():
    print(single_decreasing_term_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN))

    return


def test_single_lifelong_insurance():
    print(single_lifelong_insurance(i=I, population=POPULATION, x=X, f=F, lifespan=LIFESPAN))

    return


def test_single_increasing_lifelong_insurance():
    print(single_increasing_lifelong_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN))

    return


def test_single_decreasing_lifelong_insurance():
    print(single_decreasing_lifelong_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN))

    return
    

def test_single_continuous_term_insurance():
    print(single_continuous_term_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN))

    return


def test_single_continuous_lifelong_insurance():
    print(single_continuous_lifelong_insurance(i=I, population=POPULATION, x=X, f=F, lifespan=LIFESPAN))

    return


if __name__ == '__main__':
    test_single_term_insurance()
    print('----------------')
    test_single_life_insurance()
    print('----------------')
    test_single_endowment_insurance()
    print('----------------')
    test_single_increasing_term_insurance()
    print('----------------')
    test_single_decreasing_term_insurance()
    print('----------------')
    test_single_lifelong_insurance()
    print('----------------')
    test_single_increasing_lifelong_insurance()
    print('----------------')
    test_single_decreasing_lifelong_insurance()
    print('----------------')
    test_single_continuous_term_insurance()
    print('----------------')
    test_single_continuous_lifelong_insurance()
    print('----------------')
