# 生存人口、死亡人口の変換を実装

import numpy as np


def living_to_dead(population, lifespan=112):
    """
    生存人口を死亡人口に変換

    Parameters
    ----------
    population: ndarray<int>
        生存人口
        size: (lifespan, )
    lifespan: int, default 112
        最終年齢
    
    Returns
    -------
    dead_population: ndarray<int>
        死亡人口
        size: (lifespan, )
    """

    assert len(population.shape) == 1, '生存人口の入力が異なります'
    assert population.shape[0] == lifespan + 1, '生存人口は0歳から最終年齢分まで入力してください'

    dead_population = []

    for j in range(0, lifespan):
        dead_population.append(population[j] - population[j + 1])
    
    dead_population.append(population[lifespan])

    dead_population = np.array(dead_population)

    return dead_population