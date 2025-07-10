import streamlit as st

st.set_page_config(page_title="MBTI 여행지 추천기", page_icon="✈️")

st.title("🧠 MBTI 유형 기반 ✈️ 여행지 추천기")
st.markdown("당신의 MBTI와 원하는 도시를 선택하면, 성격에 맞는 **관광지와 맛집**을 추천해줄게요! 🌍✨")
st.balloons()

# 예시 도시 데이터
city_data = {
    "파리": {
        "INTJ": [
            {"name": "루브르 박물관", "reason": "사색을 즐기는 INTJ에게 예술과 역사 탐방은 최고의 영감이 됩니다. 🎨"},
            {"name": "생제르맹 거리", "reason": "고요하게 걷기 좋은 지적 분위기의 거리. 혼자 여행하기에 제격! 🧳"}
        ],
        "ENFP": [
            {"name": "몽마르트 언덕", "reason": "자유로운 영혼의 ENFP는 거리 공연과 예술에 흠뻑 빠질 수 있어요. 🎭"},
            {"name": "마레 지구", "reason": "작고 감성적인 카페들이 넘쳐나는 이곳은 ENFP의 에너지를 충전시켜줘요. ☕"}
        ],
        # ... 14개 MBTI 더 추가 가능
    },
    "도쿄": {
        "ISFP": [
            {"name": "요요기 공원", "reason": "자연 속에서 혼자만의 시간을 보내는 것을 좋아하는 ISFP에게 안성맞춤. 🌳"},
            {"name": "나카메구로", "reason": "감성적인 소도시 느낌의 지역으로 감각적인 카페 탐방도 좋아요. 📸"}
        ],
        "ESTJ": [
            {"name": "도쿄 타워", "reason": "계획적이고 목표 지향적인 ESTJ에게 꼭대기 전망대는 상징적인 장소예요. 🗼"},
            {"name": "츠키지 시장", "reason": "정돈되고 활기찬 시장은 ESTJ의 에너지와 딱 맞아요. 🍣"}
        ]
        # ... 14개 MBTI 더 추가 가능
    },
    # 도시 추가 가능
}

city = st.selectbox("🌆 여행하고 싶은 도시를 선택하세요", list(city_data.keys()))
mbti = st.selectbox("🧬 당신의 MBTI를 선택하세요", ["INTJ", "INTP", "ENTJ", "ENTP", "INFJ", "INFP", "ENFJ", "ENFP",
                                                  "ISTJ", "ISFJ", "ESTJ", "ESFJ", "ISTP", "ISFP", "ESTP", "ESFP"])

if st.button("🔍 여행지 추천 받기"):
    if mbti in city_data[city]:
        st.subheader(f"✈️ {city}에서 {mbti}에게 추천하는 명소는?")
        for spot in city_data[city][mbti]:
            st.markdown(f"**📍 {spot['name']}**  \n👉 {spot['reason']}")
        st.success("즐거운 여행 되세요! 🎒")
        st.balloons()
    else:
        st.warning("아직 이 조합의 데이터가 준비되지 않았어요. 곧 업데이트할게요! 🙏")
