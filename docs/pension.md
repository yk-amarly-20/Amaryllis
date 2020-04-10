# calculate present value of life annuity
```python
from amaryllis.models.pension import *
```

## ```life_annuity(i=0.03, population=POPULATION, x=30, n=20, due=True, f=10, lifespan=112)```
calculate value of life insurance annuity.  

#### parameters
・ i (float (default 0.03)) -- annual interest rate  
・ population (ndarray(int) (default POPULATION)) -- population between 0 and lifespan  
・ x (int (default 30)) -- age of an insurance contract  
・ n (int (default 20)) -- term of contract  
・ due (bool (default True)) -- whether early payment or end payment  
・ f (int (default 10)) -- deferment period  
・ lifespan (int default 112) -- final age  

#### Returns
・ a (float) -- life insurance annuity  

#### sample
```python
>>> from amaryllis.models.pension import *
>>> import numpy as np
>>> population = np.array([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0])
>>> x = 0
>>> n = 3
>>> lifespan = 10
>>> f = 0
>>> a = life_annuity(population=population, x=x, n=n, f=f, lifespan=lifespan)
>>> print("a = {}".format(a))
a = 2.6278631350739943
```

## ```lifelong_annuity(i=0.03, population=POPULATION, x=30, due=True, f=10, lifespan=112)```
calculate value of lifelong insurance annuity.  

#### parameters
・ i (float (default 0.03)) -- annual interest rate  
・ population (ndarray(int) (default POPULATION)) -- population between 0 and lifespan  
・ x (int (default 30)) -- age of an insurance contract  
・ due (bool (default True)) -- whether early payment or end payment  
・ f (int (default 10)) -- deferment period  
・ lifespan (int default 112) -- final age  

#### Returns
・ a (float) -- lifelong insurance annuity  


## ```increasing_life_annuity(i=0.03, population=POPULATION, x=30, n=20, due=True, f=10, lifespan=112)```
calculate value of increasing_life_annuity.  

#### parameters
・ i (float (default 0.03)) -- annual interest rate  
・ population (ndarray(int) (default POPULATION)) -- population between 0 and lifespan  
・ x (int (default 30)) -- age of an insurance contract  
・ n (int (default 20)) -- term of contract  
・ due (bool (default True)) -- whether early payment or end payment  
・ f (int (default 10)) -- deferment period  
・ lifespan (int default 112) -- final age  

#### Returns
・ a (float) -- life insurance annuity  


## ```increasing_lifelong_annuity(i=0.03, population=POPULATION, x=30, n=20, due=True, f=10, lifespan=112)```
calculate value of increasing lifelong annuity.  

#### parameters
・ i (float (default 0.03)) -- annual interest rate  
・ population (ndarray(int) (default POPULATION)) -- population between 0 and lifespan  
・ x (int (default 30)) -- age of an insurance contract  
・ n (int (default 20)) -- max numbers of increasing   
・ due (bool (default True)) -- whether early payment or end payment  
・ f (int (default 10)) -- deferment period  
・ lifespan (int default 112) -- final age  

#### Returns
・ a (float) -- increasing lifelong annuity   


## ```decreasing_life_annuity(i=0.03, population=POPULATION, x=30, n=20, due=True, f=10, lifespan=112)```

#### parameters
・ i (float (default 0.03)) -- annual interest rate  
・ population (ndarray(int) (default POPULATION)) -- population between 0 and lifespan  
・ x (int (default 30)) -- age of an insurance contract  
・ n (int (default 20)) -- term of contract  
・ due (bool (default True)) -- whether early payment or end payment  
・ f (int (default 10)) -- deferment period  
・ lifespan (int default 112) -- final age  

#### Returns
・ a (float) -- decreasing_life_annuity  
