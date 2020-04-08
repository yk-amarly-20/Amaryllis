# interest.pyのテストケース

import numpy as np
import sys
sys.path.append('./../../')
from Amaryllis.util.interest import *


I = 0.03
K = 4


def test_present_value_rate():
    present_value_rate(I)

    return


def test_discount_rate():
    discount_rate(I)

    return


def test_name_interest_rate():
    name_discount_rate(I, K)

    return


def test_name_discount_rate():
    name_discount_rate(I, K)

    return


def test_force_of_interest():
    force_of_interest(I)

    return


if __name__ == '__main__':
    test_present_value_rate()
    test_discount_rate()
    test_name_interest_rate()
    test_name_discount_rate()
    test_force_of_interest()