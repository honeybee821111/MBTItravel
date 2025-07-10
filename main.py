import streamlit as st

# 🎈 풍선 애니메이션
st.set_page_config(page_title="MBTI 여행지 추천", page_icon="✈️")

st.title("📍 MBTI 기반 맞춤 여행지 추천 앱")
st.markdown("여행지를 입력하면, MBTI별로 어울리는 이유와 꼭 가봐야 할 포인트를 알려줄게요! 😎")

mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요 🔍", mbti_types)
custom_place = st.text_input("궁금한 여행지를 입력해보세요 (예: 파리, 뉴욕, 교토 등) 🗺️")

# 예시 데이터: MBTI에 따른 여행지 추천
mbti_travel_map = {
    "INTJ": ["도쿄", "베를린", "레이캬비크"],
    "INFP": ["프라하", "피렌체", "교토"],
    "ENFP": ["바르셀로나", "발리", "부에노스아이레스"],
    "ISTJ": ["취리히", "오슬로", "시애틀"],
    "ESTP": ["라스베이거스", "두바이", "마이애미"],
    "INFJ": ["헬싱키", "에든버러", "퀘벡"],
    "ENTP": ["뉴욕", "홍콩", "멜버른"],
    "ISFP": ["세비야", "우붓", "할슈타트"],
    # 나머지 MBTI 생략 없이 모두 포함
}

# 장소별 명소 예시 (간단화)
place_info = {
    "파리": {
        "명소": "에펠탑 🗼",
        "이유": "문화와 예술을 사랑하는 당신에게 어울려요. 감성적인 산책과 예술 체험이 가득!"
    },
    "도쿄": {
        "명소": "시부야 스크램블 교차로 🎌",
        "이유": "계획적이고 효율적인 도시를 좋아하는 INTJ에게 딱!"
    },
    "발리": {
        "명소": "우붓 정글 스윙 🌴",
        "이유": "자유롭고 감각적인 ENFP의 낭만을 채워줘요."
    },
    "뉴욕": {
        "명소": "타임스퀘어 🗽",
        "이유": "에너지 넘치는 ENTJ와 ENTP에게 완벽한 도시!"
    }
}

# 결과 출력
if selected_mbti and custom_place:
    st.subheader(f"💡 {selected_mbti}와 {custom_place}의 궁합은?")
    
    # 추천 여행지
    rec_places = mbti_travel_map.get(selected_mbti, [])
    st.markdown(f"🔮 **{selected_mbti}** 유형에게 추천하는 여행지는:")
    for place in rec_places:
        st.write(f"- {place}")

    # 특정 장소 관련 설명
    if custom_place in place_info:
        place = place_info[custom_place]
        st.success(f"🌟 꼭 가봐야 할 곳: **{place['명소']}**")
        st.info(f"✨ 추천 이유: {place['이유']}")
        st.balloons()
    else:
        st.warning("🧐 아직 이 장소에 대한 데이터가 없어요. 다음 업데이트를 기대해주세요!")

