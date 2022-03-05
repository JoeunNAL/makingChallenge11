# 패키지 설치 : geopy , folium
# map1.html 파일 만들어주세요

import folium
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='Travel')
gallery_name = '서울시립미술관'
gallerys = geolocator.geocode(gallery_name)
gallery_latitude = gallerys.raw['lat']
gallery_longitude = gallerys.raw['lon']

# 지도 배경 생성(광화문 기준)
# Zoom : zoom_start 최대 18, 최소 0
m = folium.Map([37.5738858, 126.9748345], zoom_start=15.5)

# 마크 표시
folium.Marker(location=[gallery_latitude, gallery_longitude], popup=gallery_name,
              icon=folium.Icon(color='red')).add_to(m)
# map1.html에 표시
m.save(r'map1.html')
