# pension.pyのテスト

import numpy as np
import sys
sys.path.append('./../../')
from amaryllis.models.pension import *
from amaryllis.config import *


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
    

