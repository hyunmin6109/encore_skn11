import re
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# ✅ 크롬 드라이버 설정
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

# ✅ 크롬 드라이버 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ✅ 1. 구글 뉴스 검색 페이지로 이동
search_query = "캠핑카 판매량"
google_news_search_url = f"https://news.google.com/search?q={search_query}&hl=ko&gl=KR&ceid=KR:ko"
driver.get(google_news_search_url)
time.sleep(3)  # 초기 로딩 대기

# ✅ 2. 뉴스 기사 로드 대기
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "article"))
    )
    print("✅ 뉴스 목록 페이지 로드 완료")
except:
    print("⚠️ 뉴스 목록을 찾을 수 없습니다.")
    driver.quit()
    exit()

# ✅ 3. 뉴스 기사 100개 크롤링
news_data = []
news_articles = driver.find_elements(By.CSS_SELECTOR, "article")[:100]  # 상위 100개 기사 선택

for idx, article in enumerate(news_articles, 1):
    try:
        # ✅ 기사 제목 및 링크 추출
        news_link = article.find_element(By.TAG_NAME, "a")
        news_title = news_link.text.strip()

        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(news_link)).click()
        time.sleep(3)  # 페이지 로딩 대기

        # ✅ 새 창으로 전환
        driver.switch_to.window(driver.window_handles[-1])

        # ✅ 뉴스 본문 크롤링 (다양한 태그 탐색)
        paragraphs = driver.find_elements(By.TAG_NAME, "p")
        if not paragraphs:
            paragraphs = driver.find_elements(By.CSS_SELECTOR, "div")  # 본문이 <div>에 있을 경우
        content = "\n".join([p.text for p in paragraphs if p.text])

        # 📌 디버깅: 본문 확인
        print(f"\n📜 [기사 {idx}] 본문 미리보기:")
        print(content[:500])  # 본문이 잘 나오는지 앞 500자 출력

        # ✅ 판매량 데이터 추출 (정규식 개선 적용)
        sales_data_list = []
        sales_pattern = re.findall(r"(\d{4})\s*년[^\d]*(\d{1,3}(?:,\d{3})*|1?\d{1,4})\s*(?:대\s*(?:판매|등록|출고)?)", content)

        # 📌 디버깅: 정규식 매칭 결과 확인
        print(f"🔍 [기사 {idx}] 추출된 판매량 데이터:", sales_pattern)

        for year, sales in sales_pattern:
            sales = sales.replace(",", "").replace("만", "0000")  # 1만 → 10000 변환
            sales_data_list.append(f"{year}년 {int(sales)}대 판매")  # 문자열 형태로 저장

        # ✅ 데이터 저장
        if sales_data_list:
            news_data.append({
                "제목": news_title,
                "URL": driver.current_url,
                "판매량": "; ".join(sales_data_list)  # 여러 개일 경우 세미콜론(;)으로 구분
            })
            print(f"✅ [기사 {idx}] 판매량 데이터 저장 성공")

        # ✅ 원래 창으로 돌아가기
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    except Exception as e:
        print(f"⚠️ [{idx}] 기사 크롤링 실패: {e}")

# ✅ 크롤링 완료 후 브라우저 종료
driver.quit()

# ✅ 4. 데이터 저장 (JSON 파일)
with open("camping_car_sales.json", "w", encoding="utf-8") as f:
    json.dump(news_data, f, ensure_ascii=False, indent=4)

print("\n✅ 데이터 저장 완료: camping_car_sales.json")

# ✅ 5. 최종 데이터 출력
for news in news_data[:5]:  # 상위 5개 기사만 출력
    print("\n🔹 제목:", news["제목"])
    print("🔗 URL:", news["URL"])
    print("📊 판매량 데이터:", news["판매량"])
