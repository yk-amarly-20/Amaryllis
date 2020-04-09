# population.pyのテスト

import numpy as np
import sys
sys.path.append('./../../')
from Amaryllis.survival_rate.population import *

# テスト用の仮データ
POPULATION = np.array([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])
LIFESPAN = 10

def test_living_to_dead():
    print(living_to_dead(population=POPULATION, lifespan=LIFESPAN))

    return


if __name__ == '__main__':
    test_living_to_dead()


