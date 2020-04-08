# pension.pyのテスト

import numpy as np
import sys
sys.path.append('./../../')
from Amaryllis.models.pension import *

# テスト用の仮データ
POPULATION = np.array([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])
LIFESPAN = 10
X = 0
I = 0.03
N = 2
F = 1


def test_life_annuity():
    print(life_annuity(i=I, population=POPULATION, x=X, n=N, due=True, f=F, lifespan=LIFESPAN))
    print(life_annuity(i=I, population=POPULATION, x=X, n=N, due=False, f=F, lifespan=LIFESPAN))

    return


def test_lifelong_annuity():
    print(lifelong_annuity(i=I, population=POPULATION, x=X, due=True, f=F, lifespan=LIFESPAN))
    print(lifelong_annuity(i=I, population=POPULATION, x=X, due=False, f=F, lifespan=LIFESPAN))
    

def test_increasing_life_annuity():
    print(increasing_life_annuity(i=I, population=POPULATION, x=X, n=N, due=True, f=F, lifespan=LIFESPAN))
    print(increasing_life_annuity(i=I, population=POPULATION, x=X, n=N, due=False, f=F, lifespan=LIFESPAN))

    return


def test_increasing_lifelong_annuity():
    print(increasing_lifelong_annuity(i=I, population=POPULATION, x=X, n=N, due=True, f=F, lifespan=LIFESPAN))
    print(increasing_lifelong_annuity(i=I, population=POPULATION, x=X, n=N, due=False, f=F, lifespan=LIFESPAN))

    return
    

def test_decreasing_life_annuity():
    print(decreasing_life_annuity(i=I, population=POPULATION, x=X, n=N, due=True, f=F, lifespan=LIFESPAN))
    print(decreasing_life_annuity(i=I, population=POPULATION, x=X, n=N, due=False, f=F, lifespan=LIFESPAN))

    return


if __name__ == '__main__':
    test_life_annuity()
    print('-------------')
    test_lifelong_annuity()
    print('-------------')
    test_increasing_life_annuity()
    print('-------------')
    test_increasing_lifelong_annuity()
    print('-------------')
    test_decreasing_life_annuity()
    print('-------------')
    

