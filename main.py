import streamlit as st

st.set_page_config(
    page_title="인바디 기반 맞춤 운동 강도 안내",
    page_icon="💪",
    layout="wide",
)

st.title("💪 인바디 기반 맞춤 운동 강도 안내")
st.write(
    "인바디 결과와 운동 경험, 목표 부위를 바탕으로 운동 예시와 기본적인 운동 방법을 안내합니다. "
    "교육용 참고 도구이며 의료 진단이나 개인별 안전한 중량 처방을 대신하지 않습니다."
)

EXERCISES = {
    "상체": {
        "초급": ["벽 푸시업", "가벼운 덤벨 로우", "밴드 풀어파트"],
        "중급": ["무릎 푸시업 또는 푸시업", "덤벨 로우", "덤벨 숄더 프레스"],
        "고급": ["벤치 프레스", "랫풀다운 또는 풀업", "덤벨 숄더 프레스"],
    },
    "하체": {
        "초급": ["의자 스쿼트", "글루트 브리지", "카프 레이즈"],
        "중급": ["맨몸 스쿼트", "덤벨 런지", "글루트 브리지"],
        "고급": ["고블릿 스쿼트", "덤벨 런지", "루마니안 데드리프트"],
    },
    "코어": {
        "초급": ["버드독", "무릎 플랭크", "데드버그"],
        "중급": ["플랭크", "데드버그", "버드독"],
        "고급": ["플랭크", "사이드 플랭크", "레그 레이즈"],
    },
    "전신": {
        "초급": ["의자 스쿼트", "벽 푸시업", "제자리 걷기"],
        "중급": ["스쿼트", "푸시업 변형", "마운틴 클라이머(천천히)"],
        "고급": ["스쿼트", "푸시업", "버피(가능한 경우)"],
    },
}

INTENSITY = {
    "초급": {"sets": "2세트", "reps": "8~12회", "rest": "60~90초 휴식",
           "guide": "동작을 정확하게 익히고, 여유 있게 마칠 수 있는 강도로 시작하세요."},
    "중급": {"sets": "2~3세트", "reps": "8~12회", "rest": "60~120초 휴식",
           "guide": "마지막 반복이 힘들지만 자세를 유지할 수 있는 강도를 선택하세요."},
    "고급": {"sets": "3~4세트", "reps": "6~12회", "rest": "90~180초 휴식",
           "guide": "무게보다 정확한 자세를 우선하고, 필요하면 보조자와 함께 운동하세요."},
}

with st.form("inbody_form"):
    st.subheader("1. 인바디 정보")
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("나이", min_value=10, max_value=100, value=17, step=1)
        height = st.number_input("키 (cm)", min_value=100.0, max_value=230.0, value=170.0, step=0.5)
    with col2:
        weight = st.number_input("체중 (kg)", min_value=20.0, max_value=300.0, value=65.0, step=0.5)
        muscle = st.number_input("골격근량 (kg)", min_value=5.0, max_value=150.0, value=28.0, step=0.1)
    with col3:
        fat_mass = st.number_input("체지방량 (kg)", min_value=2.0, max_value=150.0, value=12.0, step=0.1)
        body_fat = st.number_input("체지방률 (%)", min_value=2.0, max_value=70.0, value=18.0, step=0.1)

    st.subheader("2. 운동 정보")
    experience = st.radio("운동 경험", ["초급", "중급", "고급"], horizontal=True)
    goal = st.selectbox("운동 목표", ["근력 향상", "근육량 증가", "체지방 관리", "기초 체력 향상"])
    area = st.selectbox("운동 부위", ["상체", "하체", "코어", "전신"])
    days = st.slider("주당 운동 일수", min_value=1, max_value=7, value=3)
    health_concern = st.checkbox("운동 중 통증이 있거나 건강상 주의할 점이 있어요.")

    submitted = st.form_submit_button("맞춤 운동 안내 보기")

if submitted:
    errors = []
    if muscle + fat_mass > weight * 1.15:
        errors.append("골격근량과 체지방량의 합이 체중에 비해 큽니다. 인바디 결과를 다시 확인해 주세요.")
    if fat_mass > weight:
        errors.append("체지방량은 체중보다 클 수 없습니다. 입력값을 확인해 주세요.")
    if body_fat > 60:
        errors.append("체지방률 입력값을 확인해 주세요.")

    if errors:
        for error in errors:
            st.error(error)
    else:
        bmi = weight / ((height / 100) ** 2)
        st.header("분석 결과")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("BMI", f"{bmi:.1f}")
        c2.metric("골격근량", f"{muscle:.1f} kg")
        c3.metric("체지방량", f"{fat_mass:.1f} kg")
        c4.metric("체지방률", f"{body_fat:.1f}%")

        st.caption(
            "BMI는 키와 체중으로 계산한 참고 지표이며, 근육량이나 건강 상태를 단독으로 판단하지 않습니다. "
            "청소년은 성인 BMI 기준을 그대로 적용하기 어렵습니다."
        )

        st.header("추천 운동")
        st.write(f"**운동 목표:** {goal}  |  **운동 부위:** {area}  |  **운동 경험:** {experience}")
        info = INTENSITY[experience]
        st.info(f"**기본 안내:** {info['guide']}")
        st.write(f"**권장 시작 범위(예시):** {info['sets']} · {info['reps']} · {info['rest']}")
        st.write("운동 예시:")
        for item in EXERCISES[area][experience]:
            st.write(f"- {item}")

        st.subheader("주간 계획 예시")
        st.write(f"선택한 주당 운동 일수: **{days}일**")
        if days <= 2:
            st.write("전신 위주로 운동하고, 운동 사이에 충분히 회복하는 일정을 고려하세요.")
        elif days <= 4:
            st.write("운동 부위를 나누거나 전신 운동을 번갈아 실시하고, 회복일을 확보하세요.")
        else:
            st.write("매일 고강도 근력 운동을 하기보다 강도와 부위를 조절하고 회복일을 포함하세요.")

        if health_concern:
            st.warning(
                "통증이나 건강상 우려가 있다면 해당 동작을 중단하세요. "
                "보호자·체육 교사·의료 전문가와 상의한 뒤 운동을 선택하세요."
            )

        st.subheader("안전하게 운동하기")
        st.write(
            "운동 전 5~10분 정도 가볍게 준비운동을 하고, 동작을 정확히 익히세요. "
            "날카로운 통증, 어지럼증, 흉통 또는 비정상적인 호흡 곤란이 생기면 즉시 중단하고 도움을 요청하세요."
        )
        st.caption(
            "이 결과는 입력값과 선택 항목에 따른 일반적인 운동 예시입니다. "
            "인바디 수치만으로 개인에게 안전한 중량이나 정확한 운동 강도를 결정할 수 없습니다."
        )

