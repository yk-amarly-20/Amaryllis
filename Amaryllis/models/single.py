# 一時払保険料現価

import numpy as np
import sys
sys.path.append('./../')
from amaryllis.util.calc_base import *
from amaryllis.util.interest import *
from amaryllis.survival_rate.population import *
from amaryllis.config import *


def single_term_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN):
    """
    定期保険の一時払保険料現価を算出

    Parameters
    ---------
    i: float, default 0.03
        年利率
    population: ndarray<int>, default POPULATION
        生存人口
        size: (lifespan, )
    x: int, default 30
        契約年齢
    n: int, default 20
        契約年数
    f: int, default 10
        据置期間
    lifespan: int, default 112
        最終年齢
    
    Returns
    -------
    A: float
        保険料現価
    """

    assert (population.shape[0] == lifespan + 1) and (len(population.shape) == 1), '生存人口の入力が異なります'
    assert x + f + n <= lifespan, '契約終了前に最終年齢を迎えてしまいます'
    dead_population = living_to_dead(population, lifespan)
    Dx = D(i, population[x], x)
    
    Mx = M(i, dead_population[x + f :], x + f, lifespan)
    Mx_n = M(i, dead_population[x + f + n :], x + f + n, lifespan)

    A = (Mx - Mx_n) / Dx

    return A


def single_life_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN):
    """
    生存保険の一時払い保険料現価を算出

    Parameters
    ----------
    i: float, default 0.03
        年利率
    population: ndarray<int>, default POPULATION
        生存人口　
    x: int, default 30
        契約年齢
    n: int, default 20
        契約年数
    f: int, default 10
        据置期間
    lifespan: int, default 112
        最終年齢
    
    Returns
    -------
    A: float
        保険料現価
    """

    assert (population.shape[0] == lifespan + 1) and (len(population.shape) == 1), '生存人口の入力が異なります'
    assert x + f + n <= lifespan, '契約終了前に最終年齢を迎えてしまいます'
    Dx = D(i, population[x], x)
    Dx_n = D(i, population[x + f + n], x + f + n)

    A = Dx / Dx

    return A


def single_endowment_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN):
    """
    養老保険の一時払保険現価を算出

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
        契約年数
    f: int, default 10
        据置期間
    lifespan: int, default 112
        最終年齢
    
    Returns
    -------
    A: float
        保険料現価
    """

    A = single_term_insurance(i, population, x, n, f, lifespan) + single_life_insurance(i, population, x, n, f, lifespan)

    return A


def single_increasing_term_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN):
    """
    累加定期保険の一時払い保険料現価を算出

    Parameters
    ----------
    i: float, default I
        年利率
    population: ndarray<int>, default POPULATION
        生存人口
        size: (lifespan, )
    x: int, default 30
        契約年齢
    n: int, default 20
        契約年数
    f: int, default 10
        据置期間
    lifespan: int, default 112
        最終年齢
    
    Returns
    -------
    IA: float
        保険料現価
    """

    assert (len(population.shape) == 1) and (population.shape[0] == lifespan + 1), '生存人口の入力が異なります'
    assert x + f + n <= lifespan, '契約終了前に最終年齢を迎えてしまいます'

    dead_population = living_to_dead(population, lifespan)
    Dx = D(i, population[x], x)
    Rx = R(i, dead_population[x + f :], x + f, lifespan)
    Rx_n = R(i, dead_population[x + f + n :], x + f + n, lifespan)
    Mx_n = M(i, dead_population[x + f + n :], x + f + n, lifespan)

    IA = (Rx - Rx_n - n * Mx_n) / Dx

    return IA


def single_decreasing_term_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN):
    """
    逓減定期保険一時払いの保険料現価を算出

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
        契約年数
    f: int, default 10
        据置期間
    lifespan: int, default 112
        最終年齢
    
    Returns
    -------
    DA: float
        保険料現価
    """
    
    assert (len(population.shape) == 1) and (population.shape[0] == lifespan + 1), '生存人口の入力が異なります'
    assert x + f + n + 1 <= lifespan, '契約終了前に最終年齢を迎えてしまいます'

    dead_population = living_to_dead(population, lifespan)
    Dx = D(i, population[x], x)
    Mx = M(i, dead_population[x + f :], x + f, lifespan)
    Rx_1 = R(i, dead_population[x + f + 1 :], x + f + 1, lifespan)
    Rx_n1 = R(i, dead_population[x + f + n + 1 :], x + f + n + 1, lifespan)

    DA = (n * Mx - Rx_1 + Rx_n1) / Dx

    return DA


def single_lifelong_insurance(i=I, population=POPULATION, x=X, f=F, lifespan=LIFESPAN):
    """
    終身保険の一時払い保険料現価を算出

    Parameters
    ----------
    i: float, default 0.03
        年利率
    population: ndarray<int>, default POPULATION
        生存人口
        size: (lifespan, )
    x: int, default 30
        契約年齢
    f: int, default 10
        据置期間
    lifespan: int, default 112
        最終年齢
    
    Returns
    -------
    A: float
        保険料現価
    """

    assert (len(population.shape) == 1) and (population.shape[0] == lifespan + 1), '生存人口の入力が異なります'
    assert x + f <= lifespan, '契約終了前に最終年齢を迎えてしまいます'

    dead_population = living_to_dead(population, lifespan)

    Dx = D(i, population[x], x)
    Mx = M(i, dead_population[x + f :], x + f, lifespan)

    A = Mx / Dx

    return A


def single_increasing_lifelong_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN):
    """
    累加終身保険一時払い保険料現価を算出

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
        保険料が増大する回数の上限
    f: int, default 10
        据置期間
    lifespan: int, default 112
        最終年齢
    
    Returns
    -------
    IA: float
        保険料現価
    """

    assert (len(population.shape) == 1) and (population.shape[0] == lifespan + 1), '生存人口の入力が異なります'
    assert x + f + n <= lifespan, '契約終了前に最終年齢を迎えてしまいます'
    
    dead_population = living_to_dead(population, lifespan)
    Dx = D(i, population[x], x)
    Rx = R(i, dead_population[x + f :], x + f, lifespan)
    Rx_n = R(i, dead_population[x + f + n :], x + f + n, lifespan)

    IA = (Rx - Rx_n) / Dx

    return IA


def single_decreasing_lifelong_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN):
    """
    逓減終身保険の一時払い保険料現価を算出

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
        保険料減少回数の上限
    f: int, default 10
        据置期間
    lifespan: int, default 112
        最終年齢
    
    Returns
    -------
    DA: float
        保険料現価
    """

    assert (len(population.shape) == 1) and (population.shape[0] == lifespan + 1), '生存人口の入力が異なります'
    assert x + f + n <= lifespan, '契約終了前に最終年齢を迎えてしまいます'

    dead_population = living_to_dead(population, lifespan)
    Dx = D(i, population[x], x)
    Mx = M(i, dead_population[x + f :], x + f, lifespan)
    Rx_1 = R(i, dead_population[x + 1 :], x + 1, lifespan)
    Rx_n = R(i, dead_population[x + f + n :], x + f + n, lifespan)

    DA = (n * Mx - Rx_1 + Rx_n) / Dx

    return DA


def single_continuous_term_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN):
    """
    即時払い定期保険の一時払い保険料現価を算出

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
        契約年数
    f: int, default 10
        据置年数
    lifespan: int, default 112
        最終年齢
    
    Returns
    -------
    A: float
        保険料現価
    """

    assert (len(population.shape) == 1) and (population.shape[0] == lifespan + 1), '生存人口の入力が異なります'
    assert x + f + n <= lifespan, '契約終了前に最終年齢を迎えてしまいます'

    dead_population = living_to_dead(population, lifespan)
    Dx = D(i, population[x], x)

    Mx = M_continuous(i, dead_population[x + f :], x + f, lifespan)
    Mx_n = M_continuous(i, dead_population[x + f + n :], x + f + n, lifespan)

    A = (Mx - Mx_n) / Dx

    return A


def single_continuous_lifelong_insurance(i=I, population=POPULATION, x=X, f=F, lifespan=LIFESPAN):
    """
    即時払い終身保険の一時払い保険料現価を算出

    Parameters
    ----------
    i: float, default 0.03
        年利率
    population: ndarray<int>, default POPULATION
        生存人口
        size: (lifespan, )
    x: int, default 30
        契約年齢
    f: int, default 10
        据置期間
    lifespan: int, default 112
        最終年齢
    
    Returns
    -------
    A: float
        保険料現価
    """

    assert (len(population.shape) == 1) and (population.shape[0] == lifespan + 1), '生存人口の入力が異なります'
    assert x + f <= lifespan, '契約終了前に最終年齢を迎えてしまいます'

    dead_population = living_to_dead(population, lifespan)
    Dx = D(i, population[x], x)

    Mx = M_continuous(i, dead_population[x + f :], x + f, lifespan)

    A = Mx / Dx

    return A





    