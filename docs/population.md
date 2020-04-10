# convert population to dead_population
```python
from amaryllis.survival_rate.population import *  
```

## ```living_to_dead(population, lfespan=112)```
#### Parameters
・ population (ndarray(int)) -- population between 0 and lifespan  
・ lifespan (int (default 112)) -- final age  

#### sample
```python
>>> from amaryllis.survival_rate.population import *
>>> import numpy as np
>>> population = np.array([100, 90, 80, 70, 60, 50, 40, 30, 20, 10])
>>> lifespan = 10
>>> dead_population = living_to_dead(population, lifespan)
>>> print("dead_population = {}".format(dead_population))
dead_population = [10 10 10 10 10 10 10 10 10 10]
```

