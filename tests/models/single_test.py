# single.pyのテスト

import numpy as np
import sys
sys.path.append('./../../')
from amaryllis.models.single import *
from amaryllis.config import *


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
