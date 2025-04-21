import streamlit as st

def show_faq():
    st.title("질문!!")
    
    # 지역 선택
    st.subheader("지역 선택")
    area = st.selectbox("지역을 선택하세요:", ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"])
    
    # 차종 선택
    st.subheader("차종 선택")
    vehicle_type = st.selectbox("차종을 선택하세요:", ["승용", "승합", "화물", "특수"])
    
    # 세부 카테고리 선택
    sub_category = None
    if vehicle_type == "승용":
        sub_category = st.radio("세부 유형을 선택하세요:", ["승용겸화물", "다목적", "기타"])
    elif vehicle_type == "승합":
        sub_category = st.radio("세부 유형을 선택하세요:", ["특수"])
    elif vehicle_type == "화물":
        sub_category = st.radio("세부 유형을 선택하세요:", ["일반", "덤프", "밴", "특수용도형"])
    elif vehicle_type == "특수":
        sub_category = st.radio("세부 유형을 선택하세요:", ["견인", "구난", "특수용도형"])
    
    # 선택 결과 출력
    if sub_category:
        st.write(f"### 🚗 선택한 항목: {area} 지역, {vehicle_type} - {sub_category}")
    

