import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 여행지 추천기", page_icon="🧭")
st.title("✈️ MBTI 기반 여행지 추천기")
st.markdown("당신의 성격에 꼭 맞는 여행지를 찾아드릴게요! 😎")

# 16가지 MBTI 유형별 여행지 정보 생성
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

mbti_travel_map = {}

for mbti in mbti_types:
    mbti_travel_map[mbti] = [
        {
            "place": f"추천 여행지 A for {mbti} 🌍",
            "reason": f"{mbti} 유형은 신중하고 고요한 성향을 가지므로 이곳이 잘 맞습니다.",
            "highlights": [
                f"핵심 명소 1 for {mbti} 🏞️ - 여유로운 산책로",
                f"핵심 명소 2 for {mbti} 🏰 - 역사적 유산 탐방",
                f"핵심 명소 3 for {mbti} 🌅 - 감성적인 일몰 명소"
            ]
        },
        {
            "place": f"추천 여행지 B for {mbti} 🏖️",
            "reason": f"{mbti} 유형은 내향적이면서도 창의적이기 때문에 감성적인 여행지가 어울립니다.",
            "highlights": [
                f"핵심 명소 1 for {mbti} 🎨 - 예술 거리 산책",
                f"핵심 명소 2 for {mbti} 🧘 - 조용한 힐링 스팟",
                f"핵심 명소 3 for {mbti} 📚 - 독특한 북카페 탐방"
            ]
        },
        {
            "place": f"추천 여행지 C for {mbti} 🗺️",
            "reason": f"{mbti} 유형은 탐구심이 많고 독립적인 여행을 선호합니다.",
            "highlights": [
                f"핵심 명소 1 for {mbti} 🧗 - 모험 가득한 트래킹 코스",
                f"핵심 명소 2 for {mbti} 🌋 - 자연의 경이 체험",
                f"핵심 명소 3 for {mbti} 🥾 - 현지인과의 로컬 경험"
            ]
        }
    ]

# 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", mbti_types)

if selected_mbti:
    st.balloons()
    st.subheader(f"🧳 {selected_mbti} 유형을 위한 맞춤 여행지 추천")

    for idx, rec in enumerate(mbti_travel_map[selected_mbti], 1):
        with st.expander(f"{idx}. {rec['place']}"):
            st.markdown(f"**이유:** {rec['reason']}")
            st.markdown("**꼭 가봐야 할 명소들:**")
            for highlight in rec["highlights"]:
                st.markdown(f"- {highlight}")
