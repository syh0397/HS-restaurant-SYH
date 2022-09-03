# MMM

## 1. MMM이란?

### MMM : Marketing Mix Modeling

* 마케팅의 비용 대비 효용(매출), ‘ROI’의 정량적이고 체계적인 측정을 위해 사용하는 분석 방법으로, 마케팅 비용과 매출을 인과관계로 정의하고 상관성을 밝혀내고자 하는 것
* 1980년 후반부터 이미 글로벌 소비재 기업들이 활용해왔으며, 처음으로 도입한 회사는 P&G, 크래프트, 유니레버 등이 있음
  <aside>
  💡 **왜 MMM이 중요할까요?**
  맥킨지 설문조사에 따르면,
  - 글로벌 기업 경영진의 60%는 **ROI를 계산할 수 없어** 소셜미디어 이용에 관심이 없다고 답함
  - CEO의 80%는 **마케팅 부서의 효용을 크게 느끼지 못한다**고 답함
  - CEO의 90%는 **정량적인 데이터**를 통해 의사소통하는 CFO 및 CIO를 신뢰한다고 답함
  → 따라서, 마케팅 투자에 대한 정량적인 평가는 더더욱 중요!
  </aside>

### MMM 적용 방법

* 매일 혹은 매주 마케팅 활동의 방식, 비용(=투자)은 변하기 마련이고, 그에 따라 매출도 변화함
* → 매출을 관측해서 마케팅 비용과의 인과관계를 측정(회귀분석)하면 각각의 마케팅 방식에 대한 투자가 향후 매출에 미치는 영향도 과학적으로 예측 가능
* 예시
  * 아래와 같이 마케팅 채널에 따른 비용과 매출을 주단위로 집계한 다음 회귀분석을 시도할 수 있음
  * $β1*TV + β2*SNS + β3*Web + β4*PaidSearch + … = 매출(y)$

![Imgur](https://i.imgur.com/u7WOZyz.png)

### 참고. 기존의 마케팅 투자/예산 편성 방식(without MMM)

* 비율 기반 방식(Ratio Driven)
  * 제품군들
  * 각각이 차지하는 전년 매출 비중에 따라 마케팅 예산을 분배하는 방식
    * e.g. 매출비가 A제품 : B제품 : C제품 = 5 : 3 : 2라면 예산도 5 : 3 : 2로 편성
  * 단점 : 미래 성장 기회가 반영되지 않고, 성숙 시장에만 지나친 예산이 투입될 수 있음 + 경쟁 환경의 차이가 무시됨
* 과거 투자 기반(History Plus)
  * 지난해 투자를 토대로 내년 경영 환경 & 수익성 목표를 고려해 조정하여 편성
  * 과거 투자가 잘못되었다면 더욱 악화될 수 있는 방법이나, 경영진 입장에서는 좋은 성과를 내는 제품/지역에 대해 투자를 축소하는 것이 꺼려지는 선택이기 때문에 많은 기업들이 사용하는 방식
* 가중 평균 기반(Driven by weighted average)
  * 시장규모, 성장성, 경쟁 상황 등을 정리해 매출 효과를 정량적으로 분석하며, 요인별 가중치를 결정하고 모든 요인들의 가중 평균치를 구함
  * 단점 : 가중치를 정하는 방식에 주관이 개입할 수 있음
* **각각의 방법들의 단점을 보완해서 효율 높은 마케팅 예산 편성을 위해 MMM을 한다고 이해!**

## 2. MMM사례

* 통신사의 마케팅 투자 반응곡선 사례
  * 마케팅 투자와 추가 고객 유치와의 관계를 아래와 같이 수학식으로 표현(마케팅 투자 반응곡선)하면 채널별로 추가/감소되는 마케팅 투자가 추가 고객 유치에 어떤 영향을 미치는지, 투자 수익률이 높은 채널은 어디인지 알 수 있음
  * 아래 곡선에서
    * Display, Affiliates : 초기 투자수익률은 높지만, 포화상태가 일찍 찾아옴
    * TV : 수익성을 챙기면서 추가고객 유치 가능
    * → Display, Affiliates에 투자하기 보다는 TV 광고에 투자해야 한다는 것을 알 수 있음
    * cf. Affiliates Mkt : 제휴마케팅, 매체/매체사의 실적(클릭, 구매, 조회 등)에 따라 광고비 지급하는 방식. 구글 애드센스를 생각하면 쉬울 것 같습니다!

![Imgur](https://i.imgur.com/q8rLk70.png)

## 참고. 선형회귀

### 선형회귀란 ?

* 회귀분석은 종속변수 y와 가장 비슷한 값 𝑦̂을 출력하는 함수 $f(x)$를 찾는 과정으로도 볼 수 있음!
  * 𝑦̂=𝑓(𝑥)≈𝑦
* 이때 $f(x)$가 선형함수면 이 함수를 선형회귀모형이라고 하고, 선형회귀모형을 사용하는 회귀분석을 선형회귀분석이라고 함
  * 𝑦̂=𝑤0+𝑤1𝑥1+𝑤2𝑥2+⋯+𝑤𝐷𝑥𝐷
* 다르게 표현하면, 종속변수 y와 한 개 이상의 독립변수 X와의 선형 상관 관계를 모델링 하는 것

![Imgur](https://i.imgur.com/LToBOG6.png)

### OLS(최소자승법)

* OLS(Ordinary Least Squares)는 잔차제곱합(RSS:Residual Sum of Squares)를 최소화하는 방식으로 선형회귀모형을 구하는 것
  * 잔차 : 종속변수 y와 추정치 𝑦̂의 차이 → 잔차제곱합은 이 잔차들을 말그대로 제곱해서 더한값으로, 잔차의 크기 정도로 볼 수 있음

### 알고쓰는 R-squared (결정계수, 설명력)

* 결정계수

  * 회귀모델에서 독립변수가 종속변수를 어느 정도 설명하는지를 표현하는 지표
  * 0~1의 값을 가지며, 1에 가까울 수록 설명력이 높음
    * e.g. 결정계수가 0.7이라면 독립변수들이 종속변수의 70% 정도를 설명한다고 봄
    * cf. 독립변수의 수가 증가하면 결정계수도 상승함 → 따라서 결정계수만 갖고 회귀모델을 판단하는 것은 위험!
* 의미

  * 회귀모델이 종속변수를 설명하는 비율로 생각하면 쉬운데, 차근차근 봅시다!
    * cf. yi = 실제 종속변수, y hat(𝑦̂) = 추정값, y bar(ȳ) = 종속변수 y의 평균값
    * 만약 우리가 **종속변수 y를 정말 쉽고 단순하게 추정한다면 종속변수 y들의 평균**으로 구해볼 수 있음. 즉 우리가 회귀 모델링을 한다는 것은 y bar(ȳ)보다 잘하기 위해 하는 것이고, y의 평균값인 ȳ는 베이스라인 역할
      * 그래서 우리가 만들어낸 회귀모델이 y bar(이미지의 파란선) 수준이라면 결국 베이스라인이므로 모형에 의해 설명되는 부분이 0 = SSE 0
    * 한편 우리가 너무너무 추정을 잘해서 실제 종속변수(yi)를 제대로 추정해버리면 회귀모델은 yi를 지나가겠지만, 현실적으로는 그러기 힘들고(혹은 과적합…??) yi와 y bar 사이 어딘가에서 회귀모델이 그어질 것
      * 즉 **결정계수란 우리의 회귀모델이 그냥 평균값으로 추정해버리는 것에 비해 얼마나 실제 관측값과 가깝게 추정했는지를 판단하기 위한 지표**라고 볼 수 있습니다!
* 계산
* ![Imgur](https://i.imgur.com/Aa5rv1b.png)
  이게 뭔소린데?!

  * 결과적으로 결정계수는 두 가지 방식으로 구할 수 있습니다
    * SST : 먼저 실제 관측값(yi)들과 관측값의 평균값(y bar)의 차이의 제곱합을 구합니다

      * 위에서 말했듯, 우리는 뭘해도 평균값 만큼은 추정할 수 있습니다.
      * 따라서 우리가 설명할 부분은 관측값(종속변수)와 평균값 간의 차이 입니다.
    * 1. SSE : 회귀모델과 평균값 간의 차이의 제곱합

      * Explained Sum, 결국 회귀선이 평균에 비해 얼마나 실제 관측값에 가까워지게 추정했는지, 즉 얼마나 설명했는지(explained)를 의미
    * 2. SSR : 실 관측값과 회귀모델 간의 차이의 제곱합

      * Residual Sum, 회귀선이 실제 관측값과 얼마나 차이가 나는지를 의미
    * 위 값들을 가지고 SSE/SST 혹은 1 - (SSR/SST)로 계산 가능!

      * 공식에 따라서, 우리의 회귀모델이 평균 수준이라면 SSE가 0이 되므로 R^2 = 0
      * 회귀모델이 관측값을 완벽하게 추정했다면 SSR이 0이 되므로 R^2 = 1
* 한걸음 더 : 조정된 결정계수(Adjusted R-Squared)

  * 위에서 언급한 것처럼, 독립변수의 수가 증가하면 결정계수는 증가할 수 밖에 없음
  * 따라서 독립변수가 증가하더라도 독립변수 증가에 따른 효과를 억제시키는 연산이 필요하고, 이 연산을 거친 것이 조정된 결정계수!

 ![Imgur](https://i.imgur.com/QpSSvr2.png)

* cf. n = 표본의 수, k = 독립변수의 수

# Practice

## Dataset

* 4개 컬럼으로 구성 (첫번째 컬럼은 row number)
* 각 행은 세 개의 채널(TV, Radio, Newspaper) 각각에 대한 마케팅 투자 비용과 매출(sales)로 구성되어 있음

[Advertising and Sales](https://www.kaggle.com/datasets/sazid28/advertising.csv)

## Codes

### Setup & import

```python
# Setup
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import 
df = pd.read_csv('Advertising.csv')
```

### Describe

```python
# 각 컬럼의 전반적인 값의 상태를 파악해보는법 !
# mean, std, min/max로 이상치가 있는지를 확인해볼 수 있음
df.describe()

#저는 info()도 찍어보는 편이에요 null여부랑 data type 보려고
df.info()
```

### Correlation

```python
corr = df.corr() #correlation 계산 (-> 데이터프레임으로 반환)
sns.heatmap(corr, #데이터는 위에서 계산한 correlation dataframe
            xticklabels=corr.columns, #x축 라벨 : correlation dataframe의 columns
            yticklabels=corr.columns, #y축 라벨 : correlation dataframe의 columns
            annot=True, #값 표시 여부 설정 
            cmap=sns.diverging_palette(220, 20, as_cmap=True))#두 개 색상사이의 palette 만들기 
# strong correlation between Tv and sales (0.78)
```

![Imgur](https://i.imgur.com/Vo6qlmu.png)

- df.corr()만 찍어보면 이렇게 correlation을 데이터프레임으로 얻을 수 있습니다

### Pair Plot

* pair plot은 데이터 내의 각 컬럼들을 갖고, 각 컬럼(변수)들을 갖고 만들어낼 수 있는 모든 변수 조합의 분포도를 출력하는 것

```python
sns.pairplot(df)
```

* cf. 여기 pairplot 옵션 설명이 잘 되어 있네요!
* pair-plot에서도 X variables와 Y variable를 지정해줄 수 있습니다!

```python
sns.pairplot(df, x_vars = ['TV','radio','newspaper'], y_vars='sales',size=7, kind='reg')
```

![Imgur](https://i.imgur.com/2C5T7PG.png)

### OLS(최소자승법)

* 위에서 설명한 최소자승법을 사용한 회귀모델링 + 그에 대한 summary를 보여줍니다
  * 결정계수는 0.897, 조정된 결정계수도 0.896 → 우리의 회귀모델이 종속변수인 sales를 약 90% 정도 설명한다고 볼 수 있습니다!
  * 아래 coef를 고려하면 다음과 같은 회귀식을 얻었다고 할 수 있습니다.
    * $Sales = 2.9389 + 0.0458*TV + 0.1885*Radio -0.0010*Newspaper$
    * 의외로 라디오의 효과가 좋네요…?
    * 신문은 있으나 마나… p값도 너무 크긴 하지만요!

```python
import statsmodels.formula.api as sm
model = sm.ols(formula="sales~TV+radio+newspaper", data=df).fit()
#df는 독립변수, 종속변수가 모두 포함된 데이터프레임
#formular는 종속변수와 독립변수를 지정
#fit 메서드로 모형을 추정 -> RegressionResults라는 클래스 객체로 추정 결과 출력 
print(model.summary())
```

![Imgur](https://i.imgur.com/XGgHUKk.png)

* 참고
  * sm.add_constant(x) : 상수항 컬럼 추가 (데이터프레임에 const항이 추가됨)
  * model.summary() : RegressionResults 클래스 객체의 결과 summary 메서드
  * model.predict() : model에 기반한 predict용 메서드

```sql
Dep. Variable: 종속변수

R-squared: 결정계수 - **모형의 설명력** x100해서 측정

Model: 분석모형

Adj. R-squared: 조정된 결정계수 **모형의 설명력** x100해서 측정 - 독립변수가 많아지면서 패널티가 주어지는 것

Method: 모형 계산방식

F-statistics: 모형 적합도 통계량

Prob(F-statistics): F 통계량의 유의확률

DF Residuals: 잔차의 자유도

DF Model: 모형의 매개변수 수

AIC/BIC: 여러 모형의 적합도 비교

std err: 계수 추정치의 표준오차

t: t-value 검정통계량

P>|t|: 유의확률 - p value가 매우 작아야 모형이 적합하다 - 계수도 적합하다.

[0.025 0.975]: 95% 신뢰구간 범위

Omnibus: 잔차의 왜도/첨도 검정통계량

Prob(Omnibus): Omnibus의 유의확률

Skew/Kurtosis: 왜도/첨도

Durbin-Watson: 잔차의 독립성 검정통계량

Jarque-Bera(JB): 잔차의 왜도/첨도 검정통계량

Prob(JB): JB의 유의확률

Cond. No.: 다중공선성 검정통계량
```



### Random Forest Regression

* 참고. mae = 평균절대오차 (절대 오차의 평균), 추정정확도의 척도

```python
# random Foreset model
# Setting X and y variables
X = df.loc[:, df.columns != 'sales'] #sales 제외 변수를 X variable로 정의
y = df['sales'] # sales 변수를 y variable로 정의 

# Building Random Forest model
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error as mae 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, random_state=0)
#train, test 데이터를 나누는 과정 
#test 데이터는 전체의 25%로 설정
#random_state는 난수의 seed number 
model = RandomForestRegressor(random_state=1)
model.fit(X_train, y_train)
pred = model.predict(X_test)

# Visualizing Feature Importance
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(10).plot(kind='barh',figsize=(10,10))
# TV is the most important
```

# Reference

* MMM

[[DBR] 헷갈리는 마케팅 비용의 성과 정량화할 방법, 찾고 또 찾아라](https://dbr.donga.com/article/view/1205/article_no/6500/ac/magazine)

* seaborn의 diverging paletter documentation → 색상 커스텀 하고 싶으면 참고!

[seaborn.diverging_palette - seaborn 0.11.2 documentation](https://seaborn.pydata.org/generated/seaborn.diverging_palette.html)

* 선형회귀

[선형 회귀 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%EC%84%A0%ED%98%95_%ED%9A%8C%EA%B7%80)

[데이터 사이언스 스쿨](https://datascienceschool.net/03%20machine%20learning/04.02%20%EC%84%A0%ED%98%95%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D%EC%9D%98%20%EA%B8%B0%EC%B4%88.html)

[[R] 결정계수(R-Squared)의 의미와 계산 방법](https://m.blog.naver.com/tlrror9496/222055889079)

[다중선형회귀 깃허브 설명링크 - 설유환 ](https://github.com/syh0397/Statistics_python/blob/main/11_%EB%8B%A4%EC%A4%91%ED%9A%8C%EA%B7%80%EB%B6%84%EC%84%9D(Multiple_Regression_Analysis).ipynb)
