# calculating interest and others
```
from amaryllis.util.interest import *
```

## ```present_value_rate(i=0.03)```
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


## ```discount_rate(i=0.03)```
calculate discount rate.


## ```name_interest_rate(i=0.03, k=1)```
calculate name interest rate.
#### Parameters
・ **i** (float (default 0.03)) -- annual interest rate  
・ **k** (int (default 1)) -- counts the insured pays in a year  


## ```name_discount_rate(i=0.03, k=1)```
calculte name discount rate.  


## ```force_of_interest(i=0.03)```
calculate force of interest.
