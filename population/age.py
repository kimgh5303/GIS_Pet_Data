import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 데이터 읽기
pet_data = pd.read_csv("./반려동물 유무 및 취득경로.csv", encoding='cp949')


# 필요한 컬럼 추출
age_rows = pet_data.iloc[2:8, 1].tolist()
pet_ratio_by_age = pet_data.iloc[2:8, 2].astype(float)


# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.bar(age_rows, pet_ratio_by_age, color='#E08757')
plt.title('연령별 반려동물 소유 비율')
plt.xlabel('연령대')
plt.ylabel('반려동물 소유 비율 (%)')
plt.ylim(0, 30)
plt.show()