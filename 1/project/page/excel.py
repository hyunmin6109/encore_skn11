import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl
import matplotlib.font_manager as fm

# 한글 폰트 설정 함수
def set_korean_font():
    font_path = "C:/Windows/Fonts/malgun.ttf"  # Windows의 '맑은 고딕' 폰트 경로
    plt.rc("font", family=fm.FontProperties(fname=font_path).get_name())

# 한글 폰트 적용
set_korean_font()

def show_excel():
    # 제목
    st.title("📊 시도별 차량 총합 파이 차트")

    # 파일 경로 설정
    file_path = "C:\\encore_skn11\\1\\project\\Car_list.xlsx"  # 경로 수정

    # Excel 파일 읽기
    try:
        # openpyxl 엔진을 사용하여 엑셀 파일 읽기
        df = pd.read_excel(file_path, engine="openpyxl")

        # 데이터프레임 표시
        st.write("📂 업로드한 데이터:")


        # 시도별 차량 수 합산 (각 시도가 열(column)로 존재하는 경우)
        시도_목록 = ["서울", "부산", "대구", "인천", "광주", "대전", "울산", "세종", 
                 "경기", "강원", "충북", "충남", "전북", "전남", "경북", "경남", "제주"]

        # 데이터 정리 (해당 시도 컬럼이 존재하는 경우만 선택)
        df = df[시도_목록].sum()  # 각 시도별 합계 계산

        # NaN 값이 있으면 0으로 변환
        df = df.fillna(0)

        # 파이 차트 그리기
        fig, ax = plt.subplots(figsize=(3, 3))
        ax.pie(df, labels=df.index, autopct="%1.1f%%", startangle=140)
        plt.title("시도별 차량 총합 비율")

        # Streamlit에 출력
        st.pyplot(fig)

    except Exception as e:
        st.error(f"파일을 읽는 데 오류가 발생했습니다: {e}")

