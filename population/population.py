import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 1인 가구 연령별 데이터 읽기
single_population = pd.read_csv("./1인가구(연령별).csv", encoding='utf-8')
# 자치구가 '양천구'이고 성별이 '계'인 데이터 선택
seoul_single = single_population[(single_population['자치구별(2)'] == '양천구') & (single_population['성별(1)'] == '계')]

# 자치구별 연령별 인구 데이터 읽기
total_population = pd.read_csv("./양천구 연령별 인구.csv", encoding='utf-8')
# 자치구가 '양천구'이고 성별이 '계'인 데이터 선택
seoul_total = total_population[(total_population['자치구별(2)'] == '양천구') & (total_population['성별(1)'] == '계')]


# 필요한 컬럼 추출 (세 번째 행, 네 번째 열부터)
age_columns = total_population.iloc[1, 3:].tolist()
# 시각화 등에 사용하기 적합한 형태로 변환
formatted_age_columns = [f'{age}' for age in age_columns]


# 연령별 1인 가구 수 및 연령별 총 인구 수 추출
single_population_by_age = seoul_single.iloc[0, 3:].astype(float)
total_population_by_age = seoul_total.iloc[0, 3:].astype(float)

# 연령별 1인 가구 비율 계산
single_ratio = (single_population_by_age / total_population_by_age) * 100

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.bar(formatted_age_columns, single_ratio, color='#E08757')
plt.title('양천구 1인 가구 연령별 비율')
plt.xlabel('연령대')
plt.ylabel('1인 가구 비율 (%)')
plt.show()
