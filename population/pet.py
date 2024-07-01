import folium
import pandas as pd

# 양천구 동물 등록 현황 데이터
df = pd.read_csv("./서울특별시 양천구 동물등록현황.csv", encoding='cp949')
df.head()