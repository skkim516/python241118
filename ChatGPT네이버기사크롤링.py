import requests
from bs4 import BeautifulSoup

def crawl_article_titles(url):
    """
    네이버 검색 결과에서 신문기사 제목을 크롤링하는 함수
    :param url: 크롤링할 네이버 검색 결과 URL
    :return: 기사 제목 리스트
    """
    # HTTP 요청 헤더 설정
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    # HTTP GET 요청
    response = requests.get(url, headers=headers)

    # 응답 상태 확인
    if response.status_code != 200:
        print(f"HTTP 요청 실패: {response.status_code}")
        return []

    # BeautifulSoup을 사용한 HTML 파싱
    soup = BeautifulSoup(response.text, "html.parser")

    # 기사 제목 크롤링 (Naver 구조에 맞는 CSS 선택자 사용)
    titles = []
    for title_tag in soup.select(".news_tit"):
        title = title_tag.get_text()  # 제목 텍스트 추출
        titles.append(title)

    return titles


# URL 설정
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%B0%98%EB%8F%84%EC%B2%B4"

# 크롤링 실행
article_titles = crawl_article_titles(url)

# 결과 출력
print("=== 신문기사 제목 ===")
for idx, title in enumerate(article_titles, 1):
    print(f"{idx}. {title}")
