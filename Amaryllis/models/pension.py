# 生命年金モデルを実装

import numpy as np
import sys
sys.path.append('./../../')
from amaryllis.util.interest import *
from amaryllis.util.calc_base import *
from amaryllis.config import *


def life_annuity(i=I, population=POPULATION, x=X, n=N, due=True, f=F, lifespan=LIFESPAN):
    """
    生命年金の原価を算出する(a[x : n])

    Parameters
    ----------
    i: float, default 0.03
        年利率
    population: ndarray<int>, default POPULATION
        生存人口
        size: (lifespan, )
    x: int, default 30
        契約時年齢
    n: int, default 20
        払込期間
    due: bool, default True
        trueの場合、期始払
        falseの場合、期末払
    f: int, default 10
        据置期間
    lifespan: int, default 112
        最終年齢

    Returns
    -------
    a: float
        年金現価
    """
    assert (population.shape[0] == lifespan) and (len(population.shape) == 1), '生存人口の入力が異なります'
    
    Dx = D(i, population[x], x)
    if due:  
        assert x + n + f <= lifespan, '契約終了前に最終年齢を迎えてしまいます'
        Nx = N(i, population[x + f :], x + f, lifespan)
        Nx_n = N(i, population[x + n + f :], x + n + f, lifespan)
        a = (Nx - Nx_n) / Dx

        return a

    else:
        assert x + n + f + 1 <= lifespan, '契約終了前に最終年齢を迎えてしまいます'
        Nx_1 = N(i, population[x + f + 1 :], x + f + 1, lifespan)
        Nx_n1 = N(i, population[x + n + f + 1 :], x + n + f + 1, lifespan)
        a = (Nx_1 - Nx_n1) / Dx

        return a
      

def lifelong_annuity(i=I, population=POPULATION, x=X, due=True, f=F, lifespan=LIFESPAN):
    """
    終身生命年金の現価を算出(a[x])

    Parameters
    ----------
    i: float, default 0.03
        年利率
    population: ndarray<int>, default POPULATION
        生存人口
        size: (lifespan, )
    x: int, default 30
        契約時の年齢
    due: bool, default True
        Trueなら期始払、Falseなら期末払
    f: int, default 10
        据置期間
    lifespan: int, default 112
        最終年齢
    
    Returns
    -------
    a: float
        終身生命年金現価
    """

    assert (population.shape[0] == lifespan) and (len(population.shape) == 1), '生存人口の入力が異なります'

    Dx = D(i, population[x], x)
    if due:
        assert x + f <= lifespan, '契約終了前に最終年齢を迎えてしまいます'
        Nx = N(i, population[x + f :], x + f, lifespan)
        a = Nx / Dx

        return a

    else:
        assert x + f + 1 <= lifespan, '契約終了前に最終年齢を迎えてしまいます'
        Nx_1 = N(i, population[x + f + 1 :], x + f + 1, lifespan)
        a = Nx_1 / Dx

        return a
            

def increasing_life_annuity(i=I, population=POPULATION, x=X, n=N, due=True, f=F, lifespan=LIFESPAN):
    """
    累加生命年金現価を算出(Ia[x : n])

    Parameters
    ----------
    i: float, default 0.03
        年利率
    population: ndarray<int>, default POPULATION
        生存人口
    x: int, default 30
        契約時年齢
    n: int, default 20
        払込期間
    due: bool, default True
        Trueなら期始払、Falseなら期末払
    f: int, default 10
        据置期間
    lifespan: int, default 112
        最終年齢
    
    Returns
    -------
    Ia: float
        年金現価
    """

    assert (population.shape[0] == lifespan) and (len(population.shape) == 1), '生存人口の入力が異なります'

    Dx = D(i, population[x], x)
    if due:
        assert x + f + n <= lifespan, '契約終了前に最終年齢を迎えてしまいます'
        Sx = S(i, population[x + f :], x + f, lifespan)
        Sx_n = S(i, population[x + f + n :], x + f + n, lifespan)
        Nx_n = N(i, population[x + f + n :], x + f + n, lifespan)
        Ia = (Sx - Sx_n - n * Nx_n) / Dx

        return Ia
    
    else:
        assert x + f + n + 1 <= lifespan, '契約終了前に最終年齢を迎えてしまいます'
        Sx_1 = S(i, population[x + f + 1 :], x + f + 1, lifespan)
        Sx_n1 = S(i, population[x + f + n + 1 :], x + f + n + 1, lifespan)
        Nx_n1 = N(i, population[x + f + n + 1 :], x + f + n + 1, lifespan)
        Ia = (Sx_1 - Sx_n1 - n * Nx_n1) / Dx

        return Ia


def increasing_lifelong_annuity(i=I, population=POPULATION, x=X, n=N, due=True, f=F, lifespan=LIFESPAN):
    """
    累加終身生命年金現価を算出(Ia[x])

    Parameters
    ----------
    i: float, default 0.03
        年利率
    population: ndarray<int>, default POPULATION
        生存人口
        size: (lifespan, )
    x: int, default 30
        契約年齢
    n: int, default 20
        年金額増加回数上限
    due: bool
        Trueなら期始払、Falseなら期末払
    f: int, default 10
        据置期間
    lifespan: int, default 112
        最終年齢
    
    Returns
    -------
    Ia: float
        年金現価
    """

    assert (population.shape[0] == lifespan) and (len(population.shape) == 1), '生存人口の入力が異なります'

    Dx = D(i, population[x], x)
    if due:
        assert x + f + n <= lifespan, '契約終了前に最終年齢を迎えてしまいます'
        Sx = S(i, population[x + f :], x + f, lifespan)
        Sx_n = S(i, population[x + f + n :], x + f + n, lifespan)
        Ia = (Sx - Sx_n) / Dx

        return Ia
    
    else:
        assert x + f + n + 1 <= lifespan, '契約終了前に最終年齢を迎えてしまいます'
        Sx_1 = S(i, population[x + f + 1 :], x + f + 1, lifespan)
        Sx_n1 = S(i, population[x + f + n + 1 :], x + f + n + 1, lifespan)
        Ia = (Sx_1 - Sx_n1) / Dx

        return Ia


def decreasing_life_annuity(i=I, population=POPULATION, x=X, n=N , due=True, f=F, lifespan=LIFESPAN):
    """
    累減生命年金現価を算出(Ia[x : n])

    Parameters
    ----------
    i: float, default 0.03
        年利率
    population: ndarray<int>, default POPULATION
        生存人口
    x: int, default 30
        契約時年齢
    n: int, default 20
        払込期間
    due: bool, default True
        Trueなら期始払、Falseなら期末払
    f: int, default 10
        据置期間
    lifespan: int, default 112
        最終年齢

    Returns
    -------
    Ia: float
        年金現価
    """

    assert (population.shape[0] == lifespan) and (len(population.shape) == 1), '生存人口の入力が異なります'

    Dx = D(i, population[x], x)
    if due:
        assert x + f + n + 1 <= lifespan, '契約終了前に最終年齢を迎えてしまいます'
        Sx_1 = S(i, population[x + f + 1 :], x + f + 1, lifespan)
        Sx_n1 = S(i, population[x + f + n + 1 :], x + f + n + 1, lifespan)
        Nx = N(i, population[x + f:], x + f, lifespan)
        Ia = (n * Nx - Sx_1 + Sx_n1) / Dx

        return Ia
    
    else:
        assert x + f + n + 2 <= lifespan, '契約終了前に最終年齢を迎えてしまいます'
        Sx_2 = S(i, population[x + f + 2 :], x + f + 2, lifespan)
        Sx_n2 = S(i, population[x + f + n + 2 :], x + f + n + 2, lifespan)
        Nx_1 = N(i, population[x + f + 1 :], x + f + 1, lifespan)
        Ia = (n * Nx_1 - Sx_2 + Sx_n2) / Dx
        
        return Ia