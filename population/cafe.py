import pandas as pd
import geopandas as gpd
import pydeck as pdk

# 데이터 읽기
cafe_data = pd.read_csv("./애견카페 위치.csv")

# GeoDataFrame 생성
cafe_gdf = gpd.GeoDataFrame(
    cafe_data,
    geometry=gpd.points_from_xy(cafe_data['경도'], cafe_data['위도']),
    crs='epsg:4326'
)

# 지도 시각화용 레이어 생성
layer = pdk.Layer(
    "ScatterplotLayer",
    cafe_gdf,
    get_position="[경도, 위도]",
    get_radius=100,
    get_fill_color="[255, 140, 0, 255]",
    pickable=True,
    auto_highlight=True
)

# 지도 초기 상태 설정
center = [cafe_data['경도'].mean(), cafe_data['위도'].mean()]
view_state = pdk.ViewState(
    longitude=center[0],
    latitude=center[1],
    zoom=12
)

# Deck 생성
deck = pdk.Deck(
    layers=[layer],
    initial_view_state=view_state
)

# HTML로 저장
deck.to_html("./cafe_map.html")