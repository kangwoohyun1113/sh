    },
    "고급": {
        "label": "고급 · 상대적으로 높은 강도",
        "description": "운동 기술과 지속적인 훈련 경험이 충분한 경우를 위한 단계입니다. 고급을 선택했다고 무거운 중량을 반드시 사용할 필요는 없습니다.",
        "frequency": "개인의 훈련 계획과 회복 상태에 따라 조절하며, 같은 근육 부위의 고강도 운동은 연속해서 하지 않습니다.",
    },
}


def valid_positive(value):
    return value > 0


st.title("💪 인바디 기반 맞춤 운동 강도 안내")
st.write(
    "인바디 수치와 운동 경험, 목표 부위를 바탕으로 운동 정보를 확인하는 교육용 앱입니다. "
    "결과는 참고용이며 의학적 진단이나 전문 운동처방을 대신하지 않습니다."
)

with st.form("assessment_form"):
    st.subheader("1. 인바디 정보")
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("나이", min_value=10, max_value=100, value=17, step=1)
        height = st.number_input("키 (cm)", min_value=100.0, max_value=230.0, value=170.0, step=0.5)
        weight = st.number_input("체중 (kg)", min_value=20.0, max_value=300.0, value=65.0, step=0.1)
    with col2:
        muscle = st.number_input("골격근량 (kg)", min_value=0.0, max_value=150.0, value=28.0, step=0.1)
        fat_mass = st.number_input("체지방량 (kg)", min_value=0.0, max_value=150.0, value=12.0, step=0.1)
        body_fat_pct = st.number_input("체지방률 (%)", min_value=0.0, max_value=70.0, value=18.0, step=0.1)

    st.subheader("2. 운동 경험과 목표")
    experience = st.radio(
        "최근 운동 경험을 선택하세요.",
        ["초급", "중급", "고급"],
        horizontal=True,
        help="초급: 운동을 막 시작했거나 불규칙함 / 중급: 기본 동작에 익숙하고 꾸준히 운동함 / 고급: 여러 달 이상 규칙적으로 훈련하고 동작 숙련도가 높음",
    )
    goal = st.selectbox("운동 목적", ["근력 향상", "근육량 증가", "체지방 관리", "기초 체력 향상"])
    body_part = st.selectbox("운동하고 싶은 부위", ["상체", "하체", "코어", "전신"])
    days = st.selectbox("일주일에 운동할 수 있는 날", [2, 3, 4, 5, 6], index=1)
    pain_or_condition = st.checkbox("현재 통증이 있거나 운동에 영향을 주는 건강 문제가 있습니다.")
    submitted = st.form_submit_button("운동 정보 분석하기", type="primary")

if submitted:
    errors = []
    if not valid_positive(weight):
        errors.append("체중은 0보다 커야 합니다.")
    if muscle + fat_mass > weight * 1.15:
        errors.append("골격근량과 체지방량의 합이 체중보다 크게 입력된 것 같습니다. 인바디 결과를 확인해 주세요.")
    if body_fat_pct > 70:
        errors.append("체지방률 입력값을 확인해 주세요.")

    if errors:
        for error in errors:
            st.error(error)
    else:
        st.divider()
        st.header("분석 결과")

        bmi = weight / ((height / 100) ** 2)
        c1, c2, c3 = st.columns(3)
        c1.metric("BMI", f"{bmi:.1f}", help="BMI는 체성분을 직접 구분하지 않는 참고 지표이며, 근육량이 많은 사람에게는 해석에 한계가 있습니다.")
        c2.metric("골격근량", f"{muscle:.1f} kg")
        c3.metric("체지방률", f"{body_fat_pct:.1f}%")

        st.caption(
            "인바디 값은 기기, 측정 시점, 수분 상태 등에 따라 달라질 수 있습니다. "
            "체지방률과 골격근량은 나이와 성별 등 여러 요소를 고려해야 하므로 이 앱은 수치만으로 정상/비정상을 진단하지 않습니다."
        )

        st.subheader("운동 강도 및 빈도 안내")
        info = INTENSITY_INFO[experience]
        st.info(f"**{info['label']}**\n\n{info['description']}\n\n{info['frequency']}")
        st.write(f"**선택한 목표:** {goal}  |  **운동 부위:** {body_part}  |  **희망 빈도:** 주 {days}일")

        if pain_or_condition:
            st.warning(
                "통증 또는 건강 문제가 있다고 선택했습니다. 통증을 유발하는 운동은 피하고, "
                "운동 시작 전 의료진 또는 자격을 갖춘 운동 전문가에게 상담하세요."
            )

        st.subheader(f"{body_part} 추천 운동 예시 · {experience}")
        for item in EXERCISES[body_part][experience]:
            with st.container(border=True):
                st.markdown(f"**{item['name']}**")
                a, b, c = st.columns(3)
                a.write(f"세트: {item['sets']}")
                b.write(f"반복/시간: {item['reps']}")
                c.write(f"휴식: {item['rest']}")
                st.write(item["note"])

        st.subheader("운동량 조절 방법")
        st.write(
            "처음에는 제시된 운동의 가장 낮은 반복 횟수나 짧은 시간부터 시작하세요. "
            "운동 중 자세가 무너지거나 평소와 다른 통증, 어지럼증, 흉통, 비정상적인 호흡곤란이 나타나면 즉시 중단하고 필요한 도움을 받으세요. "
            "운동이 편안하게 느껴지고 회복이 충분할 때만 한 번에 한 요소(반복 횟수, 시간 또는 무게)를 조금씩 늘리세요."
        )
        st.caption(
            "이 앱은 운동 경험 선택에 따라 예시 운동을 제시합니다. 인바디 결과만으로 안전한 중량이나 정확한 운동량을 계산하지 않으며, "
            "실제 운동 강도는 건강 상태, 기술, 피로도, 회복 상태에 따라 달라집니다."
        )
