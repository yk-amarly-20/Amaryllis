# 計算基数を実装
import numpy as np
from python.util.interest import *


def D(i, l, x):
    """
    Dxを実装

    Parameters
    ----------
    i: float
        年利率
    l: int
        x年における生存数
    x: int
        年

    Returns
    -------
    D: float
        Dxの計算基数
    """

    v = present_value_rate(i)
    D = (v ** x) * l

    return D
