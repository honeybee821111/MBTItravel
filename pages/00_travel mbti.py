import streamlit as st
import pandas as pd

# 실제 명소 + 맛집 데이터 (일부 MBTI 유형 샘플)
city_data = {
    "파리": {
        "INTJ": {
            "landmarks": [
                {"name": "루브르 박물관", "reason": "지적 호기심이 많은 INTJ에게 완벽한 예술 탐방지 🎨", "lat": 48.8606, "lon": 2.3376},
                {"name": "에펠탑", "reason": "계획적이고 구조적인 미를 사랑하는 INTJ에게 적합 🗼", "lat": 48.8584, "lon": 2.2945},
                {"name": "오르세 미술관", "reason": "논리와 감성을 함께 충족시키는 인상파의 세계 🖼️", "lat": 48.8600, "lon": 2.3266}
            ],
            "foods": [
                {"name": "Le Meurice Alain Ducasse", "reason": "정제된 경험을 추구하는 INTJ에게 이상적 🍽️", "lat": 48.8655, "lon": 2.3285},
                {"name": "Pierre Hermé", "reason": "절제된 감성 안의 혁신적인 디저트를 위한 마카롱 🍰", "lat": 48.8529, "lon": 2.3332}
            ]
        }
    },
    "도쿄": {
        "ENFP": {
            "landmarks": [
                {"name": "시부야 스크램블", "reason": "도시의 역동성과 군중의 에너지를 즐기는 ENFP 🌆", "lat": 35.6595, "lon": 139.7005},
                {"name": "하라주쿠", "reason": "창의성을 자극하는 거리 문화 🎨", "lat": 35.6703, "lon": 139.7020},
                {"name": "요요기 공원", "reason": "에너지를 충전할 수 있는 자유로운 공원 🌳", "lat": 35.6728, "lon": 139.6949}
            ],
            "foods": [
                {"name": "Ichiran Ramen", "reason": "분위기마저 특별한 1인 라멘 경험 🍜", "lat": 35.6581, "lon": 139.7007},
                {"name": "Uobei Sushi", "reason": "움직이는 스시 트레인이 호기심 자극 🍣", "lat": 35.6593, "lon": 139.6982}
            ]
        }
    },
    "뉴욕": {
        "INFP": {
            "landmarks": [
                {"name": "센트럴 파크", "reason": "자연과 고요함 속 사색을 위한 공원 🌿", "lat": 40.7851, "lon": -73.9683},
                {"name": "첼시 마켓", "reason": "감성을 자극하는 아티스틱한 시장 🛍️", "lat": 40.7424, "lon": -74.0060},
                {"name": "MoMA", "reason": "창의력과 내면의 미학을 즐기는 공간 🎨", "lat": 40.7614, "lon": -73.9776}
            ],
            "foods": [
                {"name": "By Chloe", "reason": "비건 감성의 건강한 메뉴 🥗", "lat": 40.7295, "lon": -73.9846},
                {"name": "Joe's Pizza", "reason": "전통과 향수를 느낄 수 있는 따뜻한 공간 🍕", "lat": 40.7306, "lon": -74.0027}
            ]
        }
    },
    "런던": {
        "ISTP": {
            "landmarks": [
                {"name": "대영박물관", "reason": "지식과 구조적 사고를 중시하는 ISTP 🏺", "lat": 51.5194, "lon": -0.1270},
                {"name": "캠든 마켓", "reason": "자유로운 탐색을 즐기기에 최적 🌆", "lat": 51.5416, "lon": -0.1432},
                {"name": "테이트 모던", "reason": "실험정신을 존중하는 현대미술 공간 🖼️", "lat": 51.5076, "lon": -0.0994}
            ],
            "foods": [
                {"name": "Flat Iron", "reason": "합리적 가격과 품질의 실용주의식 스테이크 🥩", "lat": 51.5145, "lon": -0.1337},
                {"name": "Dishoom", "reason": "감각적 인도 퓨전으로 색다른 경험 🍛", "lat": 51.5263, "lon": -0.0771}
            ]
        }
    },
    "로마": {
        "ESFJ": {
            "landmarks": [
                {"name": "콜로세움", "reason": "이야기를 좋아하는 ESFJ에겐 생생한 역사 🏛️", "lat": 41.8902, "lon": 12.4922},
                {"name": "트레비 분수", "reason": "로맨틱하고 감성적인 장소 💦", "lat": 41.9009, "lon": 12.4833},
                {"name": "바티칸", "reason": "공동체와 의미를 중요시하는 사람을 위한 공간 ⛪", "lat": 41.9029, "lon": 12.4534}
            ],
            "foods": [
                {"name": "Roscioli", "reason": "로컬의 정과 고급 요리의 조화 🍝", "lat": 41.8946, "lon": 12.4729},
                {"name": "Pizzarium", "reason": "친숙하고 품질 높은 로마식 피자 🍕", "lat": 41.9109, "lon": 12.4545}
            ]
        }
    },
    "시드니": {
        "ENTP": {
            "landmarks": [
                {"name": "오페라 하우스", "reason": "표현력과 창의력을 자극하는 공간 🎭", "lat": -33.8568, "lon": 151.2153},
                {"name": "본다이 비치", "reason": "에너지 넘치는 해변 🌊", "lat": -33.8908, "lon": 151.2743},
                {"name": "록스 마켓", "reason": "새로운 것 탐색에 딱 맞는 곳 🛍️", "lat": -33.8599, "lon": 151.2091}
            ],
            "foods": [
                {"name": "The Grounds", "reason": "브런치와 창의적인 공간 ☕", "lat": -33.9105, "lon": 151.2005},
                {"name": "Mr. Wong", "reason": "도전적이고 감각적인 아시아 퓨전 🍜", "lat": -33.8642, "lon": 151.2071}
            ]
        }
    },
    "홍콩": {
        "ISFJ": {
            "landmarks": [
                {"name": "빅토리아 피크", "reason": "안정감을 주는 도시 전망 🏞️", "lat": 22.2758, "lon": 114.1455},
                {"name": "만모 사원", "reason": "영성과 전통의 조화 🌸", "lat": 22.2849, "lon": 114.1501},
                {"name": "스타 페리", "reason": "전통적인 감성을 자극하는 페리 ⛴️", "lat": 22.2945, "lon": 114.1695}
            ],
            "foods": [
                {"name": "Tim Ho Wan", "reason": "가성비 좋은 딤섬 🥟", "lat": 22.3171, "lon": 114.1703},
                {"name": "Mak's Noodle", "reason": "전통 완탕면의 맛 🍜", "lat": 22.2815, "lon": 114.1551}
            ]
        }
    }
}

# 인터페이스
st.set_page_config(page_title="MBTI 세계 여행지 추천", page_icon="🗺️")
st.title("✈️ MBTI 기반 세계 도시 여행 & 맛집 추천기")
st.markdown("여행할 도시와 MBTI를 선택하면, 성격에 맞는 장소와 지도로 안내해드려요! 🌍")

selected_city = st.selectbox("🌆 도시를 선택하세요", list(city_data.keys()))
selected_mbti = st.selectbox("🧬 MBTI 유형을 선택하세요", ["INTJ", "INFP", "ENFP", "ISTP", "ESFJ", "ENTP", "ISFJ"])

if st.button("🔍 추천 보기"):
    try:
        places = city_data[selected_city][selected_mbti]
        st.balloons()

        st.subheader("📍 추천 관광지")
        for spot in places["landmarks"]:
            st.markdown(f"**{spot['name']}**  \n👉 {spot['reason']}")

        st.subheader("🍽️ 추천 맛집")
        for food in places["foods"]:
            st.markdown(f"**{food['name']}**  \n👉 {food['reason']}")

        st.subheader("🗺️ 지도 보기")
        locations = places["landmarks"] + places["foods"]
        map_df = pd.DataFrame([{"lat": loc["lat"], "lon": loc["lon"]} for loc in locations])
        st.map(map_df)

    except:
        st.warning("죄송해요, 이 조합의 데이터는 아직 준비 중이에요. 😥")
