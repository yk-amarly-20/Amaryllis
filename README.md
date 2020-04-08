# Amaryllis

### 保険料現価を算出するアクチュアリー業務用モジュールです。

①一時払い保険料現価  
Amaryllis.models.singleをimport  
パラメータは、それぞれ  

i: 年利率  
population: 0歳から最終年齢までの生存人口(ndarray)  
x: 契約年齢  
n: 契約年数  
f: 据置期間, デフォルトは0(据置なし)  
lifespan: 最終年齢, デフォルトは112歳





