# 인디드 페이지에서 봇을 통한 웹 스크랩을 금지시켰기 때문에 브라우저로 우회하여 접속할수 있도록
#셀레니움을 사용하였다.
from selenium import webdriver  #웹브라우저는 파이썬에서 브라우저를 실행할 수 있는 방법
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from requests import get
from extractors.wwr import extract_wwr_job

browser = webdriver.Chrome() # 크롬브라우저를 만들었다
browser.get("https://kr.indeed.com/jobs?q=python&l=&vjk=bf2320f2ad1232a9") # 만든 크롬 브라우저에 원하는 페이지의 주소를 넣어줌
# print(browser.page_source) # 뷰티풀 수프에 전달하기 위한 html을 뽑아옴

soup = BeautifulSoup(browser.page_source,"html.parser") # 리퀘스트가 아니라 셀레늄으로 사용할땐 .page_source를 사용함 request를 사용할땐 .text를 사용한다
job_list = soup.find("ul", class_="jobsearch-ResultsList")# 인디드에서 직업 게시판 불러옴
jobs = job_list.find_all("li", recursive=False) # 게시판 내의 리스트들이 li로 되어있어서 불러온다 하지만 li 안에도 다른 li들이 존재하기 때문에 바로 아래단계의 li만 불러올 수 있도록 recursive=False를 해준다 

results = []                                                # 다른 li가 존재하는지 여부는 len을 사용하여 갯수를 확인해보면 이상하다는 점을 알 수 있음
for job in jobs:
    zone = job.find("div",class_="mosaic-zone") # .find 로 값을 찾게되면 element(요소) 혹은 None으로 값을 찾아준다 // None은 무언가 있어야하는데 없다고 나타내는 데이터 타입이다
    if zone == None:
        anchor = job.select_one("h2 a") #job이 none이라면 job에서 select_one해서 h2부분에서 a을 선택하여 가져와서 anchor에 저장하라는 뜻 // select와 select_one의 차이는 반환값의 형태와 갯수이다 / select는 리스트로 반환 select_one은 단일요소로 반환
        title = anchor['aria-label'] # 뷰티풀 수프는 데이터의 구조를 리스트 or 딕셔너리로 바꿀 수 있기때문에 이렇게 가져올 수 있다  
        link = anchor['href']
        company = job.find("span",class_="companyName")
        location = job.find("div",class_="companyLocation")

# 딕셔너리 형태로 만들어 저장 하고 밖에 만든 result리스트에 저장한다
        job_data = {'link':f"https://kr.indeed.com{link}" ,
                    'company': company.string,
                     'location': location.string,
                      'position': title }
        results.append(job_data)
        # print(title, link)
        # print("////////\n///////")
        # print("")
for result in results:
    print(result, "////////\n//////////")        


# soup = BeautifulSoup(browser.page_source, "html.parser")
# job_list = soup.find("ul", class_="jobsearch-ResultsList")
# jobs = job_list.find_all("li", recursive=False)
# print(len(jobs))


# 창이 실행되었다가 종료되는 이유는 크롬드라이버의 버전이 정확히 일치하지 않으면 자동 종료된다
# 그래서 대기를 무한정 걸어주는 코드를 아래 작성한다
while (True):
    pass