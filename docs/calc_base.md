# calculate commutation column
```python
from amaryllis.util.calc_base import *
```

## ```D(i, population, x)```
#### Parameters
・ **i** (float) -- annual interest rate  
・ **population** (int) -- living population in x  
・ **x** (int) -- age
#### Returns
・ **D** (float) -- commutation column of D  
#### sample
```python
>>> from amaryllis.util.calc_base import *
>>> i = 0.03
>>> population = 100
>>> x = 30
>>> Dx = D(i, population, x)
>>> print("Dx = {}".format(Dx))
Dx = 41.19867595159069
```


## ```N(i, population, x, lifespan=112)```
#### Parameters
・ **i** (float) -- annual interest rate
・ **population** (ndarray<int>)
