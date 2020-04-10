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
・ **population** (ndarray(int)) -- population between x and lifespan every year  
・ **x** (int) -- age  
・ **lifespan** (int (default 112)) -- final age  

#### Returns
・ **N** (float) -- commutation column of N  

## ```C(i, dead_population, x)```
#### Parameters
・ **i** (float) -- annual interest rate   
・ **dead_population** (int) -- numbers which died between x and (x+1)    
・ **x** (int) -- age  

#### Returns
・ **C** (float) -- commutation column of C  



## ```M(i, dead_population, x, lifespan=112)```
#### Parameters
・ **i** (float) -- annual interest rate    
・ **dead_population** (ndarray(int)) -- numbers which died between x and lifespan every year  
・ **x** (int) -- age  
・ **lifespan** (int (default 112)) -- final age  

#### Returns
・ M (float) -- commutation column of M  

## ```S(i, population, x, lifespan=112)``` 
#### Parameters
・ **i** (float) -- annual interest rate    
・ **population** (ndarray(int)) -- population between x and lifespan every year  
・ **x** (int) -- age  
・ **lifespan** (int (default 112)) -- final age  

#### Returns
・ **S** (float) -- commutation column of S    


## ```R(i, dead_population, x, lifespan=112)```
#### Parameters
・ **i** (float) -- annual interest rate    
・ **dead_population** (ndarray(int)) -- numbers which died between x and lifespan every year  
・ **x** (int) -- age  
・ **lifespan** (int (default 112)) -- final age  

#### Returns
・ R (float) -- commutation column of R  


## ```C_continuous(i, dead_population, x)```
#### Parameters
・ **i** (float) -- annual interest rate   
・ **dead_population** (int) -- numbers which died between x and (x+1)    
・ **x** (int) -- age  

#### Returns
・ **C** (float) -- commutation column of continuous C  


## ```M_continuous(i, dead_population, x, lifespan=112)```
#### Parameters
・ **i** (float) -- annual interest rate    
・ **dead_population** (ndarray(int)) -- numbers which died between x and lifespan every year  
・ **x** (int) -- age  
・ **lifespan** (int (default 112)) -- final age  

#### Returns
・ M (float) -- commutation column of continuous M  



