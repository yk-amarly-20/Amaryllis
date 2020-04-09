## calculating interest and others
```
from amaryllis.util.interest import *
```

### present_value_rate(i=0.03)
calculate present value rate.

#### Parameters
・ **i** (int (default 0.03)) -- annual interest rate

#### sample
```python
>>> from amaryllis.util.interest import *
>>> v = present_value_rate()
>>> print("v = {}".format(v))
v = 0.970873786407767
```


### discount_rate(i=0.03)
・ **i** (int (default 0.03)) -- annual interest rate

#### sample
