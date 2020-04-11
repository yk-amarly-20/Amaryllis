# calculate value of single payment insurance  

## ```single_term_insurance(i=0.03, population=POPULATION, x=30, n=20, f=10, lifespan=112)```
calculate value of single payment term insurance.  

#### Parameters
・ i (float (default 0.03)) -- annual interest rate  
・ population (ndarray(int) (default POPULATION)) -- population between 0 and lifespan  
・ x (int (default 30)) -- age of an insurance contract  
・ n (int (default 20)) -- term of contract  
・ f (int (default 10)) -- deferment period  
・ lifespan (int default 112) -- final age  

#### Returns
・ A (float) -- single payment term insurance.  

##### sample
```python
>>> from amaryllis.models.single import *
>>> import numpy as np
>>> population = np.array([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0])
>>> i = 0.03
>>> x = 0
>>> n = 3
>>> f = 1
>>> lifespan = 10
>>> A = single_term_insurance(i=i, population=population, x=x, n=n, f=f, lifespan=lifespan)
>>> print("A = {}".format(A))
A = 0.2746224616402602
```



## ```single_life_insurance(i=0.03, population=POPULATION, x=30, n=20, f=10, lifespan=112)```  
calculate value of single payment life insurance.  

#### Parameters
・ i (float (default 0.03)) -- annual interest rate  
・ population (ndarray(int) (default POPULATION)) -- population between 0 and lifespan  
・ x (int (default 30)) -- age of an insurance contract  
・ n (int (default 20)) -- term of contract  
・ f (int (default 10)) -- deferment period  
・ lifespan (int default 112) -- final age  

#### Returns
・ A (float) -- single payment life insurance.  


## ```single_endowment_insurance(i=0.03, population=POPULATION, x=30, n=20, f=10, lifespan=112)```   
calculate value of single payment endowment insurance.(term_insurance + life insurance)  

#### Parameters
・ i (float (default 0.03)) -- annual interest rate  
・ population (ndarray(int) (default POPULATION)) -- population between 0 and lifespan  
・ x (int (default 30)) -- age of an insurance contract  
・ n (int (default 20)) -- term of contract  
・ f (int (default 10)) -- deferment period  
・ lifespan (int default 112) -- final age  

#### Returns
・ A (float) -- single payment endowment insurance.   


## ```single_increasing_term_insurance(i=0.03, population=POPULATION, x=30, n=20, f=10, lifespan=112)```  
calculate value of single payment increasing term insurance.  

#### Parameters
・ i (float (default 0.03)) -- annual interest rate  
・ population (ndarray(int) (default POPULATION)) -- population between 0 and lifespan  
・ x (int (default 30)) -- age of an insurance contract  
・ n (int (default 20)) -- term of contract  
・ f (int (default 10)) -- deferment period  
・ lifespan (int default 112) -- final age  

#### Returns
・ IA (float) -- single payment increasing term insurance.  


## ```single_decreasing_term_insurance(i=0.03, population=POPULATION, x=30, n=20, f=10, lifespan=112)```  
calculate value of single payment decreasing term insurancne.  

#### Parameters
・ i (float (default 0.03)) -- annual interest rate  
・ population (ndarray(int) (default POPULATION)) -- population between 0 and lifespan  
・ x (int (default 30)) -- age of an insurance contract  
・ n (int (default 20)) -- term of contract  
・ f (int (default 10)) -- deferment period  
・ lifespan (int default 112) -- final age  

#### Returns
・ DA (float) -- single payment decreasing term insurance.  


## ```single_lifelong_insurance(i=0.03, population=POPULATION, x=30, f=10, lifespan=112)```  
calculate value of single payment lifelong insurancne.  

#### Parameters
・ i (float (default 0.03)) -- annual interest rate  
・ population (ndarray(int) (default POPULATION)) -- population between 0 and lifespan  
・ x (int (default 30)) -- age of an insurance contract  
・ f (int (default 10)) -- deferment period  
・ lifespan (int default 112) -- final age  

#### Returns
・ A (float) -- single payment lifelong insurance.  


##  ```single_increasing_lifelong_insurance(i=0.03, population=POPULATION, x=30, n=20, f=10, lifespan=112)```  
calculate value of single payment increasing lifelong insurancne.    

#### Parameters
・ i (float (default 0.03)) -- annual interest rate  
・ population (ndarray(int) (default POPULATION)) -- population between 0 and lifespan  
・ x (int (default 30)) -- age of an insurance contract  
・ n (int (defualyt 20)) -- max numbers of increasing  
・ f (int (default 10)) -- deferment period  
・ lifespan (int default 112) -- final age  

#### Returns
・ IA (float) -- single payment increasing lifelong insurance.  

## ```single_decreasing_lifelong_insurance(i=I, population=POPULATION, x=X, n=N, f=F, lifespan=LIFESPAN)```  
calculate value of single payment decreasing lifelong insurancne.  

#### Parameters
・ i (float (default 0.03)) -- annual interest rate  
・ population (ndarray(int) (default POPULATION)) -- population between 0 and lifespan  
・ x (int (default 30)) -- age of an insurance contract  
・ n (int (defualyt 20)) -- max numbers of decreasing  
・ f (int (default 10)) -- deferment period  
・ lifespan (int default 112) -- final age  

#### Returns
・ DA (float) -- single payment decreasing lifelong insurance.   

## ```single_continuous_term_insurance(i=0.03, population=POPULATION, x=30, n=20, f=10, lifespan=112)```  
calculate value of single payment continuous term insurancne.  


#### Parameters
・ i (float (default 0.03)) -- annual interest rate  
・ population (ndarray(int) (default POPULATION)) -- population between 0 and lifespan  
・ x (int (default 30)) -- age of an insurance contract  
・ n (int (default 20)) -- term of contract  
・ f (int (default 10)) -- deferment period  
・ lifespan (int default 112) -- final age  

#### Returns
・ A (float) -- single payment continuous term insurance.  


## ```single_continuous_lifelong_insurance(i=0.03, population=POPULATION, x=30, f=10, lifespan=112)```   
calculate value of single payment continuous lifelong insurancne.   

#### Parameters
・ i (float (default 0.03)) -- annual interest rate  
・ population (ndarray(int) (default POPULATION)) -- population between 0 and lifespan  
・ x (int (default 30)) -- age of an insurance contract   
・ f (int (default 10)) -- deferment period  
・ lifespan (int default 112) -- final age  

#### Returns
・ A (float) -- single payment continuous lifelong insurance.   

