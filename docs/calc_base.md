# calculate commutation column
```python
from amaryllis.util.calc_base import *
```

## ```D(i, population, x)```
#### Parameters
・ **i** (float) -- annual interest rate
・ **population** (population) -- living population in x
・ **x** (int) -- age
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
