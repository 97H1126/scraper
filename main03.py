from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_job

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

respones = get(f"{base_url}{search_term}")

if respones.status_code != 200:
    print("코드를 불러올 수 없습니다")

else : 
    print(respones.text) 

#indeed 사이트에서 봇으로 인식하여 접근할수가 없음