# 利息計算を行う
import numpy as np


def present_value_rate(i=0.03):
    """
    現価率を計算

    Parameters
    ----------
    i: float, default 0.03
        年利率

    Returns
    -------
    v: float
        現価率
    """

    v = 1 / (1 + i)

    return v


def discount_rate(i=0.03):
    """
    割引率を計算

    Parameters
    ----------
    i: float, default 0.03
        年利率

    Returns
    -------
    d: float
        割引率
    """

    d = i / (1 + i)

    return d


def name_interest_rate(i=0.03, k=1):
    """
    名称利率を計算

    Parameters
    ----------
    i: float, default 0.03
        年利率
    k: int, default 1
        一年に支払う回数

    Returns
    -------
    i_k: float
        年k回払いの名称利率
    """

    i_k = k * ((1 + i) ** (1 / k) - 1)

    return i_k


def name_discount_rate(i=0.03, k=1):
    """
    名称割引率を計算

    Parameters
    ----------
    i:　float, default 0.03
        年利率
    k: int, default 1
        一年に支払う回数

    Returns
    -------
    d_k: float
        年k回払いの名称割引率
    """

    i_k = name_interest_rate(i, k)

    d_k = i_k / (1 + i_k / k)

    return d_k


def force_of_interest(i=0.03):
    """
    利力を計算

    Parameters
    ----------
    i: float, default 0.03
        年利率

    Returns
    -------
    delta: float
        利力
    """

    delta = np.log(1 + i)

    return delta
