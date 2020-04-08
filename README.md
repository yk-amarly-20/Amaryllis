# Amaryllis

### 保険料現価を算出するアクチュアリー業務用モジュールです。

## ①保険金現価
Amaryllis.models.singleをimport  
パラメータは、それぞれ  

i: 年利率  
population: 0歳から最終年齢までの生存人口(ndarray)  
x: 契約年齢  
n: 契約年数  
f: 据置期間, デフォルトは0(据置なし)  
lifespan: 最終年齢, デフォルトは112歳  

例) i = 0.03 (3%)  
population = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]  
x = 0 (0歳契約)  
n = 3 (三年契約)  
f = 1 (一年据置)  
lifespan = 10 (最終年齢10歳) <- あり得ませんが、とりあえず例として 


・ 定期保険  
single_term_insurance(i, population, x, n, f, lifespan)  

・ 生存保険  
single_life_insurance(i, population, x, n, f, lifespan)  

・ 養老保険  
single_endowment_insurance(i, population, x, n, f, lifespan)  

・ 逓増定期保険  
single_increasing_term_insurance(i, population, x, n, f, lifespan)  

・ 逓減定期保険  
single_decreasing_term_insurance(i, population, x, n, f, lifespan)  

・ 終身保険  
single_lifelong_insurance(i, population, x, f, lifespan)  

・ 逓増終身保険
single_increasing_lifelong_insurance(i, population, x, n, f, lifespan)  

・ 逓減終身保険  
single_decreasing_lifelong_insurance(i, population, x, n, f, lifespan)  

・ 即時払い定期保険  
single_continuous_term_insurance(i, population, x, n, f, lifespan)  

・ 即時払い終身保険  
single_continuous_lifelong_insurance(i, population, x, f, lifespan)  








