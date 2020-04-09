## calculating interest and others
```
from amaryllis.util.interest import *
```

### present_value_rate(i=0.03)
calculate present value rate.

#### Parameters
・ **i** (float (default 0.03)) -- annual interest rate

#### sample
```python
>>> from amaryllis.util.interest import *
>>> v = present_value_rate()
>>> print("v = {}".format(v))
v = 0.970873786407767
```


### discount_rate(i=0.03)
・ **i** (float (default 0.03)) -- annual interest rate


### name_interest_rate(i=0.03, k=1)
・ **i** (float (default 0.03)) -- annual interest rate  
・ **k** (int (default 1)) -- counts the insured pays in a year