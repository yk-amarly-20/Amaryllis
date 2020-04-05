# 生命年金モデルを実装

import numpy as np
import sys
sys.path.append('./../')
from util.interest import *
from util.calc_base import *


def life_annuity(i, population, x, n, lifespan=112, due=True):
    """
    生命年金の原価を算出する(a[x : n])

    Parameters
    ----------
    i: float
        年利率
    population: ndarray<int>
        生存人口
        size: (lifespan, )
    x: int
        契約時年齢
    n: int
        払込期間
    lifespan: int, default 112
        最終年齢
    due: bool, default True
        trueの場合、期始払
        falseの場合、期末払

    Returns
    -------
    a: float
        年金現価
    """
    assert (population.shape[0] == lifespan) and (len(population.shape) == 1), '生存人口の入力が異なります'
    
    Dx = D(i, population[x], x)
    if due:
        assert x + n <= lifespan, 'x+n年後に最終年齢を超えてしまいます'
        Nx = N(i, population[x :], x, lifespan)
        Nx_n = N(i, population[x + n :], x + n, lifespan)
        a = (Nx - Nx_n) / Dx

        return a
    
    else:
        assert x + n + 1 <= lifespan, 'x+n+1年後に最終年齢を超えてしまいます'
        Nx_1 = N(i, population[x + 1 :], x + 1, lifespan)
        Nx_n1 = N(i, population[x + n + 1 :], x + n + 1, lifespan)
        a = (Nx_1 - Nx_n1) / Dx

        return a


def lifelong_annuity(i, population, x, lifespan=112, due=True):
    """
    終身生命年金の現価を算出(a[x])

    Parameters
    ----------
    i: float
        年利率
    population: ndarray<int>
        生存人口
        size: (lifespan, )
    x: int
        契約時の年齢
    lifespan: int, default 112
        最終年齢
    due: bool, default True
        Trueなら期始払、Falseなら期末払
    
    Returns
    -------
    a: float
        終身生命年金現価
    """

    assert (population.shape[0] == lifespan) and (len(population.shape) == 1), '生存人口の入力が異なります'

    Dx = D(i, population[x], x)
    if due:
        assert x <= lifespan, '最終年齢より前に契約してください'
        Nx = N(i, population, x, lifespan)
        a = Nx / Dx

        return a

    else:
        assert x + 1 <= lifespan, '最終年齢より前に契約してください'
        Nx_1 = N(i, population[x + 1 :], x + 1, lifespan)
        a = Nx_1 / Dx

        return a
  

def increasing_life_annuity(i, population, x, n, lifespan=112, due=True):
    """
    累加生命年金現価を算出(Ia[x : n])

    Parameters
    ----------
    i: float
        年利率
    population: ndarray<int>
        生存人口
    x: int
        契約時年齢
    n: int
        払込期間
    lifespan: int, default 112
        最終年齢
    due: bool, default True
        Trueなら期始払、Falseなら期末払
    
    Returns
    -------
    Ia: float
        年金現価
    """

    assert (population.shape[0] == lifespan) and (len(population.shape) == 1), '生存人口の入力が異なります'

    Dx = D(i, population[x], x)
    if due:
        assert x + n <= lifespan, 'x+n年後に最終年齢を超えてしまいます'
        Sx = S(i, population[x:], x, lifespan)
        Sx_n = S(i, population[x + n :], x + n, lifespan)
        Nx_n = N(i, population[x + n :], x + n, lifespan)
        Ia = (Sx - Sx_n - n * Nx_n) / Dx

        return Ia
    
    else:
        assert x + n + 1 <= lifespan, 'x+n+1年後に最終年齢を超えてしまいます'
        Sx_1 = S(i, population[x + 1 :], x + 1, lifespan)
        Sx_n1 = S(i, population[x + n + 1 :], x + n + 1, lifespan)
        Nx_n1 = N(i, population[x + n + 1 :], x + n + 1, lifespan)
        Ia = (Sx_1 - Sx_n1 - n * Nx_n1) / Dx

        return Ia


def increasing_lifelong_annuity(i, population, x, n, lifespan=112, due=True):
    """
    累加終身生命年金現価を算出(Ia[x])

    Parameters
    ----------
    i: float
        年利率
    population: ndarray<int>
        生存人口
        size: (lifespan, )
    x: int
        契約年齢
    n: int
        年金額増加回数上限
    lifespan: int, default 112
        最終年齢
    due: bool
        Trueなら期始払、Falseなら期末払
    
    Returns
    -------
    Ia: float
        年金現価
    """

    assert (population.shape[0] == lifespan) and (len(population.shape) == 1), '生存人口の入力が異なります'

    Dx = D(i, population[x], x)
    if due:
        assert x + n <= lifespan, 'x+n年後に最終年齢を超えてしまいます'
        Sx = S(i, population[x:], x, lifespan)
        Sx_n = S(i, population[x + n :], x + n, lifespan)
        Ia = (Sx - Sx_n) / Dx

        return Ia
    
    else:
        assert x + n + 1 <= lifespan, 'x+n+1年後に最終年齢を超えてしまいます'
        Sx_1 = S(i, population[x + 1 :], x + 1, lifespan)
        Sx_n1 = S(i, population[x + n + 1 :], x + n + 1, lifespan)
        Ia = (Sx_1 - Sx_n1) / Dx

        return Ia



        
        
        

    

    
        

        
        




