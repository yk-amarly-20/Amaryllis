# 計算基数を実装
import numpy as np
import sys
sys.path.append('./../')
from amaryllis.util.interest import *


def D(i, population, x):
    """
    Dxを実装

    Parameters
    ----------
    i: float
        年利率
    population: int
        x年における生存数
    x: int
        年

    Returns
    -------
    D: float
        Dxの計算基数
    """

    v = present_value_rate(i)
    D = (v ** x) * population

    return D


def Nc(i, population, x, lifespan=112):
    """
    Nxを実装
    x年から最終年齢までの、Dxの和

    Parameters
    ----------
    i: float
        年利率
    population: ndarray<int>
        生存人口　
    x: int
        最初の年
    lifespan: int, default 112
        最終年齢

    Returns
    -------
    N: float
        Nxの計算基数  
    """

    assert (population.shape[0] == lifespan - x + 1) and (len(population.shape) == 1), "生存人口の入力数が異なります"

    Dxs = [D(i, p, y) for y, p in zip(range(x, lifespan + 1), population)]
    Dxs = np.array(Dxs)

    N = np.sum(Dxs)

    return N


def C(i, dead_population, x):
    """
    Cxの計算基数を実装

    Parameters
    ----------
    i: float
        年利率
    dead_population: int
        x年度死亡人口
    x: int
        最初の年

    Returns
    -------
    C: float
        Cxの計算基数
    """

    v = present_value_rate(i)
    C = v ** (x + 1) * dead_population

    return C


def M(i, dead_population, x, lifespan=112):
    """
    Mの計算基数を計算
    Cxの最終年齢までの和

    Parameters
    ----------
    i: float
        年利率
    dead_population: ndarray<int>
        x~lifespan年度死亡人口
        size: (lifespan - x, )
    x: int
        最初の年度
    lifespan: int, default 112
        最終年齢

    Returns
    -------
    M: float
        Mxの計算基数
    """

    assert (dead_population.shape[0] == lifespan - x + 1) and (len(dead_population.shape) == 1), "死亡人口の入力が異なります"

    Cxs = [C(i, p, y) for y, p in zip(range(x, lifespan + 1), dead_population)]
    Cxs = np.array(Cxs)

    M = np.sum(Cxs)

    return M


def S(i, population, x, lifespan=112):
    """
    Sxの計算基数を実装
    Mxの最終年齢までの和

    Parameters
    ----------
    i: float
        年利率
    population: ndarray<int>
        x~lifespan年度生存人口
        size: (lifespan - X, )
    x: int
        最初の年
    lifespan: int, default 120
        最終年齢

    Returns
    -------
    S: float
        Sxの計算基数
    """

    assert (population.shape[0] == lifespan - x + 1) and (len(population.shape) == 1), "生存人口の入力数が異なります"

    S = 0

    for j in range(0, lifespan - x):
        S += (j + 1) * D(i, population[j], j)

    return S


def R(i, dead_population, x, lifespan=112):
    """
    Rの計算基数を実装
    Mxの最終年齢までの和

    Parameters
    ----------
    i: float
        年利率
    dead_population: ndarray<int>
        x~lifespan年度までの死亡人口
    x: int
        最初の年
    lifespan: int, default 120
        最終年齢

    Returns
    -------
    R: float
        Rの計算基数
    """

    assert (dead_population.shape[0] == lifespan - x + 1) and (len(dead_population.shape) == 1), "死亡人口の入力が異なります"

    R = 0
    for j in range(0, lifespan - x):
        R += (j + 1) * C(i, dead_population[j], j)

    return R


def C_continuous(i, dead_population, x):
    """
    C_の計算基数を実装

    Parameters
    ----------
    i: float
        年利率
    dead_population: int
        死亡人口
    x: int
        年度

    Returns
    -------
    C: float
        C_の計算基数
    """

    v = present_value_rate(i)
    C = v ** (x + 1 / 2) * dead_population

    return C


def M_continuous(i, dead_population, x, lifespan=112):
    """
    M_の計算基数を実装

    Parameters
    ----------
    i: float
        年利率
    dead_population: ndarray<int>
        x~lifespan年度における死亡人口
    x: int
        最初の年度
    lifespan: int, default 120
        最終年齢

    Returns
    -------
    M: float
        M_の計算基数
    """

    assert (dead_population.shape[0] == lifespan - x + 1) and (len(dead_population.shape) == 1), "死亡人口の入力が異なります"

    Cxs = [C_continuous(i, p, y) for y, p in zip(
        range(x, lifespan + 1), dead_population)]
    Cxs = np.array(Cxs)

    M = np.sum(Cxs)

    return M
