import streamlit as st

st.set_page_config(
    page_title="FITMATE | 맞춤 운동 플래너",
    page_icon="💪",
    layout="wide"
)

# 운동 앱 느낌의 다크 네이비 + 라임 포인트 디자인
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Pretendard:wght@400;500;600;700;800;900&display=swap');
:root {--lime:#b8f34a; --panel:#142238; --line:#2b3c55;}
.stApp {
    background: radial-gradient(ellipse at 12% 0%, rgba(184,243,74,.10), transparent 30%),
                linear-gradient(180deg, #0b1220 0%, #0d1728 100%);
    color:#f4f7fb; font-family:'Pretendard',sans-serif;
}
.block-container {max-width:1180px; padding-top:2rem; padding-bottom:4rem;}
h1,h2,h3,p,label,.stMarkdown {font-family:'Pretendard',sans-serif;}
h1 {font-weight:900 !important; letter-spacing:-1.5px;}
h2 {font-weight:800 !important; letter-spacing:-.6px;}
[data-testid="stMetric"] {
    background:linear-gradient(145deg,#18263b,#111c2e);
    border:1px solid #2b3c55; border-radius:18px; padding:18px 20px;
}
[data-testid="stMetricLabel"] {color:#aab8ca !important;}
[data-testid="stMetricValue"] {color:#c7ff68 !important; font-weight:850;}
div[data-testid="stExpander"] {background:#121f33; border:1px solid #2b3c55; border-radius:14px;}
.stTextInput input,.stNumberInput input,.stSelectbox div[data-baseweb="select"],.stTextArea textarea {
    background-color:#142238 !important; color:#f4f7fb !important;
    border-color:#344963 !important; border-radius:11px !important;
}
.stRadio label,.stCheckbox label {color:#e5edf7 !important;}
.stButton button {background:#b8f34a; color:#14200b; border:0; border-radius:12px; font-weight:800;}
.stButton button:hover {background:#d0ff7b; color:#14200b;}
hr {border-color:#2b3c55 !important;}
[data-testid="stAlert"] {border-radius:14px;}
.fit-hero {
    padding:30px 32px; margin:0 0 26px; border-radius:24px; overflow:hidden;
    background:linear-gradient(115deg,#1b2d42 0%,#142238 58%,#243a27 100%);
    border:1px solid #3b5364; position:relative;
}
.fit-hero:after {
    content:"FIT"; position:absolute; right:24px; bottom:-42px;
    font-size:150px; line-height:1; font-weight:900;
    color:rgba(184,243,74,.08); letter-spacing:-12px;
}
.fit-kicker {color:#c5fa6c; font-size:12px; font-weight:900; letter-spacing:2px; margin-bottom:10px;}
.fit-title {color:white; font-size:clamp(28px,4vw,42px); line-height:1.15; font-weight:900; letter-spacing:-1.5px; margin-bottom:10px;}
.fit-desc {color:#bdcadd; font-size:15px; max-width:680px; line-height:1.7;}
.fit-pill {
    display:inline-block; margin-top:17px; padding:7px 12px; border-radius:999px;
    background:rgba(184,243,74,.13); color:#d2ff8c;
    border:1px solid rgba(184,243,74,.35); font-size:12px; font-weight:800;
}
.section-tag {color:#c5fa6c; font-size:11px; font-weight:900; letter-spacing:1.8px; margin-bottom:3px;}
.fit-note {
    padding:14px 17px; background:#142238; border:1px solid #2d425e;
    border-left:4px solid #b8f34a; border-radius:12px; color:#c5d1e0;
    line-height:1.65; margin:12px 0 20px;
}
footer,#MainMenu {visibility:hidden;}
</style>
<div class="fit-hero">
  <div class="fit-kicker">YOUR PERSONAL TRAINING COMPANION</div>
  <div class="fit-title">FITMATE<br>나에게 맞는 운동을 시작하다.</div>
  <div class="fit-desc">인바디 데이터와 운동 경험, 운동 환경을 바탕으로<br>나에게 맞는 운동 방향과 루틴을 찾아보세요.</div>
  <span class="fit-pill">BODY ANALYSIS · CUSTOM WORKOUT · PROGRESS</span>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="fit-note">💡 인바디 정보와 운동 경험, 운동 장소를 함께 고려해 운동 목표와 시작 운동량을 추천합니다. '
    '결과는 참고용이며 인바디 수치만으로 운동 능력이나 안전한 강도를 확정할 수 없습니다.</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="section-tag">01 / BODY DATA</div>', unsafe_allow_html=True)
st.subheader("인바디 정보 입력")
c1, c2, c3 = st.columns(3)
with c1:
    height = st.number_input("키 (cm)", min_value=100.0, max_value=230.0, value=170.0, step=0.5)
    weight = st.number_input("체중 (kg)", min_value=25.0, max_value=250.0, value=65.0, step=0.5)
with c2:
    muscle = st.number_input("골격근량 (kg)", min_value=5.0, max_value=100.0, value=27.0, step=0.1)
    body_fat = st.number_input("체지방률 (%)", min_value=2.0, max_value=65.0, value=22.0, step=0.1)
with c3:
    sex = st.selectbox("체지방률 참고 범위", ["남성 기준", "여성 기준", "기준 적용하지 않음"])
    age = st.number_input("나이", min_value=13, max_value=100, value=17, step=1)

st.caption("입력값은 본인의 인바디 결과지에 적힌 수치를 사용하세요. 성별 기준은 참고용이며 개인차가 있습니다.")

st.markdown('<div class="section-tag">02 / TRAINING PROFILE</div>', unsafe_allow_html=True)
st.subheader("운동 환경과 경험")
c4, c5, c6 = st.columns(3)
with c4:
    place = st.radio("주로 운동할 장소", ["헬스장", "집"], horizontal=True)
with c5:
    experience = st.selectbox(
        "운동 경험",
        ["초급 (운동을 거의 하지 않음)", "중급 (몇 달 이상 꾸준히 운동)", "고급 (오랜 기간 규칙적으로 운동)"]
    )
with c6:
    goal = st.selectbox("운동 목표", ["근력과 근육량 향상", "체지방 관리", "전반적인 체력 향상"])

part = st.selectbox("운동하고 싶은 부위", ["전신", "상체", "하체", "코어"])
health_note = st.checkbox("운동할 때 통증, 어지럼증 또는 의료진의 운동 제한이 있음")
st.divider()

# 입력값으로 계산한 참고 지표
height_m = height / 100
bmi = weight / (height_m ** 2)
muscle_ratio = muscle / weight * 100

if sex == "남성 기준":
    fat_status = "높은 편" if body_fat >= 25 else ("낮은 편" if body_fat < 8 else "일반 참고 범위")
elif sex == "여성 기준":
    fat_status = "높은 편" if body_fat >= 35 else ("낮은 편" if body_fat < 18 else "일반 참고 범위")
else:
    fat_status = "성별 기준을 적용하지 않음"

if bmi < 18.5:
    bmi_status = "저체중 범위"
elif bmi < 23:
    bmi_status = "일반 참고 범위"
elif bmi < 25:
    bmi_status = "과체중 참고 범위"
else:
    bmi_status = "높은 BMI 범위"

st.markdown('<div class="section-tag">03 / BODY INSIGHT</div>', unsafe_allow_html=True)
st.subheader("인바디 기반 몸 상태 분석")
m1, m2, m3 = st.columns(3)
m1.metric("BMI", f"{bmi:.1f}", bmi_status)
m2.metric("골격근량 비율", f"{muscle_ratio:.1f}%", "골격근량 ÷ 체중")
m3.metric("체지방률", f"{body_fat:.1f}%", fat_status)

st.write("**현재 수치 해석**")
if bmi < 18.5:
    st.write("- BMI가 낮은 범위입니다. 체중을 더 줄이는 것보다 충분한 식사와 점진적인 근력 운동을 우선 고려하세요.")
elif bmi >= 25:
    st.write("- BMI가 높은 범위입니다. BMI는 근육량도 반영하지 못하므로 단독 판단은 피하고, 관절 부담이 적은 운동부터 선택하세요.")
else:
    st.write("- BMI는 일반 참고 범위입니다. 이 수치만으로 체력이나 건강 상태를 판단할 수 없으므로 체지방률과 골격근량을 함께 살펴보세요.")

if fat_status == "높은 편":
    st.write("- 입력한 체지방률은 선택한 참고 기준에서 높은 편입니다. 체지방 관리가 목표라면 근력 운동과 무리 없는 유산소 활동을 함께 계획할 수 있습니다.")
elif fat_status == "낮은 편":
    st.write("- 입력한 체지방률은 선택한 참고 기준에서 낮은 편입니다. 과도한 운동이나 식사 제한보다 회복과 충분한 영양 섭취를 챙기세요.")
else:
    st.write("- 체지방률은 참고용 지표입니다. 측정 오차와 개인차가 있어 한 번의 수치만으로 몸 상태를 확정하지 마세요.")

if muscle_ratio < 35:
    st.write("- 체중 대비 골격근량 비율이 상대적으로 낮게 계산되었습니다. 이 계산은 표준 진단 지표가 아니므로, 운동 계획에서는 올바른 자세와 점진적인 근력 향상을 우선합니다.")
else:
    st.write("- 체중 대비 골격근량 비율을 참고해 근력 향상 여부를 추적할 수 있습니다. 이 비율만으로 근육량이 충분한지 판단할 수는 없습니다.")

st.markdown('<div class="section-tag">04 / YOUR WORKOUT</div>', unsafe_allow_html=True)
st.subheader("맞춤 운동 추천")
level = "초급" if experience.startswith("초급") else ("중급" if experience.startswith("중급") else "고급")
level_settings = {
    "초급": {"sets": 2, "reps": "8~12회", "rest": 75, "effort": "편안한 강도 (마지막에도 3~4회 더 할 수 있는 정도)"},
    "중급": {"sets": 3, "reps": "8~12회", "rest": 75, "effort": "중간 강도 (마지막에 2~3회 더 할 수 있는 정도)"},
    "고급": {"sets": 3, "reps": "6~12회", "rest": 90, "effort": "중간~높은 강도 (자세가 유지되는 범위)"}
}
settings = level_settings[level]

# 인바디 목표 보정: 경험 수준을 대체하지 않고 운동 구성과 휴식/선택에 반영
adjustments = []
if goal == "체지방 관리" or fat_status == "높은 편":
    adjustments.append("체지방 관리 목표를 고려해 근력 운동과 저충격 유산소 운동을 병행하는 방향으로 구성합니다.")
if muscle_ratio < 35 or goal == "근력과 근육량 향상":
    adjustments.append("근력 향상을 우선해 정확한 자세와 꾸준한 기록을 강조합니다. 초반부터 무게를 크게 올리지 않습니다.")
if bmi >= 25:
    adjustments.append("BMI가 높은 범위이므로 점프 등 충격이 큰 동작보다 통증 없는 범위의 저충격 동작을 우선 고려합니다.")
if bmi < 18.5:
    adjustments.append("BMI가 낮은 범위이므로 운동량을 급격히 늘리지 않고 회복과 충분한 영양 섭취를 함께 챙깁니다.")
if not adjustments:
    adjustments.append("현재 입력값에서는 운동 경험 수준에 맞춰 시작하고, 수행 난이도와 회복 상태에 따라 조금씩 조정합니다.")

st.info(
    f"**추천 시작 수준: {level}**  \n"
    f"운동 경험이 기본 시작 난이도를 결정하고, 인바디 지표와 목표는 운동 구성·주의점·운동량 조정에 반영됩니다."
)
for item in adjustments:
    st.write(f"- {item}")

if health_note:
    st.warning("통증, 어지럼증 또는 의료진의 제한이 있다면 강도 높은 운동을 시작하지 말고 의료진이나 운동 전문가와 먼저 상의하세요.")

# 장소/부위/경험에 따른 운동 데이터
workouts = {
    "헬스장": {
        "상체": [
            ("랫풀다운", "등", "바를 가슴 윗부분 방향으로 당기고 어깨를 으쓱하지 않습니다."),
            ("체스트 프레스 머신", "가슴", "손목을 곧게 유지하고 팔꿈치를 과하게 뒤로 보내지 않습니다."),
            ("시티드 케이블 로우", "등", "허리를 과하게 젖히지 말고 팔꿈치를 몸통 옆으로 당깁니다."),
            ("덤벨 숄더 프레스", "어깨", "가벼운 무게로 시작하고 허리를 과하게 꺾지 않습니다."),
            ("덤벨 컬", "팔", "팔꿈치를 몸 옆에 고정하고 몸을 흔들어 올리지 않습니다."),
            ("벤치프레스", "가슴", "발을 바닥에 두고 손목을 세우며, 처음에는 보조자와 가벼운 무게를 사용합니다."),
            ("덤벨 원암 로우", "등", "등을 중립으로 유지하고 몸통을 비틀어 무게를 들지 않습니다.")
        ],
        "하체": [
            ("레그 프레스", "허벅지·엉덩이", "무릎이 발끝 방향을 향하게 하고 허리가 말릴 만큼 깊게 내리지 않습니다."),
            ("레그 컬 머신", "허벅지 뒤", "반동 없이 천천히 굽히고 펴세요."),
            ("덤벨 고블릿 스쿼트", "하체", "발바닥 전체로 지지하고 무릎이 안쪽으로 무너지지 않게 합니다."),
            ("덤벨 루마니안 데드리프트", "엉덩이·허벅지 뒤", "등을 중립으로 유지하고 엉덩이를 뒤로 보내며 내려갑니다."),
            ("카프 레이즈 머신", "종아리", "반동을 줄이고 위아래 움직임을 통제합니다.")
        ],
        "코어": [
            ("플랭크", "복부", "허리가 처지거나 엉덩이가 과하게 올라가지 않게 유지합니다."),
            ("케이블 팔로프 프레스", "몸통 안정성", "몸통이 회전하지 않게 복부에 힘을 줍니다."),
            ("캡틴스 체어 니 레이즈", "복부", "반동을 쓰지 말고 허리 통증이 있으면 중단합니다."),
            ("데드버그", "복부·몸통 안정성", "허리가 과하게 뜨지 않는 범위에서 팔과 다리를 움직입니다.")
        ],
        "전신": [
            ("레그 프레스", "하체", "무릎이 발끝 방향을 향하게 하고 허리가 말릴 만큼 깊게 내리지 않습니다."),
            ("체스트 프레스 머신", "가슴·팔", "손목을 곧게 유지하고 무게를 통제합니다."),
            ("랫풀다운", "등·팔", "바를 목 뒤가 아닌 가슴 앞쪽으로 당깁니다."),
            ("덤벨 고블릿 스쿼트", "전신·하체", "발바닥 전체로 지지하고 무릎 정렬을 유지합니다."),
            ("케이블 로우", "등", "허리를 과하게 젖히지 않고 팔꿈치를 당깁니다.")
        ]
    },
    "집": {
        "상체": [
            ("벽 푸시업", "가슴·팔", "몸을 일직선으로 유지하고 팔꿈치를 약간 대각선 방향으로 굽힙니다."),
            ("무릎 푸시업", "가슴·팔", "머리부터 무릎까지 일직선을 유지하고 허리가 처지지 않게 합니다."),
            ("일반 푸시업", "가슴·팔", "손은 어깨보다 약간 넓게 두고 몸통을 일직선으로 유지합니다."),
            ("물병 숄더 프레스", "어깨", "가벼운 물병으로 시작하고 허리를 꺾지 않습니다."),
            ("철봉 매달리기", "악력·어깨 주변", "안정적인 철봉을 사용하고 어깨에 통증이 생기면 즉시 내려옵니다."),
            ("파이크 푸시업", "어깨·팔", "엉덩이를 들어 올리고 머리를 바닥에 세게 부딪치지 않도록 천천히 수행합니다.")
        ],
        "하체": [
            ("의자 스쿼트", "허벅지·엉덩이", "의자에 가볍게 앉았다 일어나며 무릎이 안쪽으로 모이지 않게 합니다."),
            ("글루트 브리지", "엉덩이", "허리를 꺾기보다 엉덩이에 힘을 주어 골반을 들어 올립니다."),
            ("리버스 런지", "하체", "균형을 잡고 앞쪽 무릎이 안쪽으로 무너지지 않게 합니다."),
            ("스플릿 스쿼트", "하체", "처음에는 벽이나 의자를 잡고 안정적으로 수행합니다."),
            ("싱글 레그 글루트 브리지", "엉덩이", "골반이 한쪽으로 기울지 않는 범위에서 수행합니다."),
            ("스쿼트", "하체", "발바닥 전체로 지지하고 통증 없는 범위에서 내려갑니다.")
        ],
        "코어": [
            ("버드독", "몸통 안정성", "허리가 돌아가지 않게 유지하고 팔과 반대쪽 다리를 뻗습니다."),
            ("데드버그", "복부", "허리가 과하게 뜨지 않는 범위에서 천천히 움직입니다."),
            ("플랭크", "복부", "허리가 처지지 않게 복부와 엉덩이에 힘을 줍니다."),
            ("사이드 플랭크(무릎)", "옆구리", "어깨 아래에 팔꿈치를 두고 몸통이 앞으로 돌아가지 않게 합니다."),
            ("레그 레이즈(무릎 굽힘)", "복부", "허리가 뜨면 다리를 덜 내리고 통증이 있으면 중단합니다.")
        ],
        "전신": [
            ("의자 스쿼트", "하체", "의자에 가볍게 앉았다 일어나며 무릎 정렬을 유지합니다."),
            ("벽 푸시업", "상체", "몸을 일직선으로 유지하고 통제된 속도로 수행합니다."),
            ("글루트 브리지", "엉덩이", "허리를 꺾지 말고 엉덩이에 힘을 줍니다."),
            ("버드독", "몸통 안정성", "골반과 몸통이 흔들리지 않게 합니다."),
            ("제자리 걷기", "유산소·전신", "균형을 유지하며 편안한 속도로 시작합니다.")
        ]
    }
}

exercise_list = workouts[place][part]
if level == "초급":
    selected = exercise_list[:4]
elif level == "중급":
    selected = exercise_list[1:6] if len(exercise_list) >= 6 else exercise_list
else:
    selected = exercise_list[2:] if len(exercise_list) > 4 else exercise_list

# 목표/체성분에 따라 추천 운동 구성을 추가로 조정
if goal == "체지방 관리" or fat_status == "높은 편":
    if place == "집":
        cardio = ("제자리 걷기", "유산소·전신", "대화가 가능한 속도로 시작하고 무릎이나 발목에 통증이 있으면 중단합니다.")
    else:
        cardio = ("실내 자전거", "저충격 유산소", "가벼운 저항으로 시작하고 숨이 너무 차면 속도를 낮춥니다.")
    if all(x[0] != cardio[0] for x in selected):
        selected = selected[:4] + [cardio]

st.write(f"**장소:** {place} · **부위:** {part} · **경험 수준:** {level} · **목표:** {goal}")
st.write(f"**권장 시작 구성:** 운동당 {settings['sets']}세트 · {settings['reps']} · 세트 사이 휴식 {settings['rest']}초")
st.write(f"**강도 기준:** {settings['effort']}")
st.caption("모든 운동은 자세가 무너지기 전에 세트를 끝내세요. 정해진 횟수가 쉽고 통증 없이 수행될 때만 다음 운동에서 횟수나 무게를 조금씩 늘립니다.")

for i, (name, focus, instruction) in enumerate(selected, start=1):
    with st.expander(f"{i}. {name} — {focus}", expanded=(i == 1)):
        st.write(f"**운동 방법 및 자세 주의:** {instruction}")
        st.write(f"**권장량:** {settings['sets']}세트 · {settings['reps']}")
        if name in ["벤치프레스", "덤벨 루마니안 데드리프트", "파이크 푸시업", "철봉 매달리기"]:
            st.write("**추가 주의:** 처음에는 낮은 난이도 또는 보조를 이용하고, 통증이 있으면 즉시 중단하세요.")

st.markdown('<div class="section-tag">05 / RECOMMENDATION LOGIC</div>', unsafe_allow_html=True)
st.subheader("추천 결과 분석")
st.write(
    f"- **경험 수준({level})**은 기본 세트 수와 반복 범위, 휴식 시간을 정했습니다.\n"
    f"- **체지방률({body_fat:.1f}%)과 목표({goal})**는 체지방 관리가 필요한 경우 저충격 유산소 운동을 추가하는 데 반영했습니다.\n"
    f"- **BMI({bmi:.1f})**는 운동 선택 시 충격 부담과 점진적 시작에 대한 주의사항에 반영했습니다.\n"
    f"- **골격근량({muscle:.1f}kg)**과 체중 대비 비율은 근력 향상 목표와 자세·기록 관리 안내에 반영했습니다."
)
st.caption(
    "주의: BMI와 체지방률의 참고 구간은 개인 진단이 아닙니다. 성장기, 임신, 질환, 부상, 약물 복용 여부에 따라 적절한 운동은 달라질 수 있습니다. "
    "운동 중 통증·어지럼증·가슴 통증이 나타나면 즉시 중단하고 전문가와 상담하세요."
)
