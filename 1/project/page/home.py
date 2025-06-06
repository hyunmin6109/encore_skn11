import streamlit as st

def show_home():
    st.title("특수차 등록 현황 및 기업 FAQ 조회 시스템")
    
    # 프로젝트 필요성 내용
    st.header("프로젝트 필요성")

    st.write("**① 특수차량(구급차·캠핑카 등)의 증가와 데이터 관리 부족**")
    st.write(
        "- 최근 캠핑 문화 확산과 응급의료 서비스 강화로 개조 특수차량(캠핑카, 구급차 등) 등록이 지속적으로 증가하고 있음\n"
        "- 그러나 개조 차량의 등록·관리 데이터는 일반 승용차보다 체계적으로 정리되지 않아, 정확한 통계를 확인하기 어려움"
    )

    st.write("**② 산업 변화와 정보 비대칭 문제**")
    st.write(
        "- 자동차 개조 시장이 성장하며 관련 기업과 소비자가 늘어나지만, 등록 절차, 법적 규정, 유지·보수 정보에 대한 공식적인 정보가 부족함\n"
        "- 기업이 제공하는 FAQ나 고객 지원 정보도 흩어져 있어, 소비자가 필요한 정보를 찾는 데 어려움을 겪음"
    )

    st.write("**③ 체계적인 정보 제공 시스템 필요**")
    st.write(
        "현재 자동차 등록 통계는 연도별·지역별 단순 집계에 머물러 있으며, 개조 차량을 포함한 특수차량의 변동 추이, 사용 패턴을 효과적으로 분석하기 어려움\n"
        "**→** 이에 따라 특수차 등록 현황을 한눈에 확인하고, 관련 기업의 FAQ 데이터를 연계하여 제공하는 시스템이 필요함"
    )
