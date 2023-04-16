from requests import get
from bs4 import BeautifulSoup

base_url = "https://www.work.go.kr/wnSearch/unifSrch.do?topQuery="
destination = "파이썬"
result = get(f"{base_url}{destination}")

if result.status_code != 200:
    print("데이터를 받을 수 없습니다")

else :
    S=BeautifulSoup(result.text,'html.parser')
    # print(S)

    jobs=S.find_all('div',class_="result-recruit-list")
    # print(len(jobs))

    for jobs in jobs:
        job_info=jobs.find_all("li")

        #여기서부터 문제임 주소 못뽑음
        for A in job_info:
            job=A.find_all("div",class_="link")
            print(job)
            # exit()

        #print(len(job_info))
        #exit()
        # for job in job_info:
        #     a=job.find_all("li")
        #     print(a)
        

            for link in job_info:
                links = link.find_all("a")
                print(links["href"])
                # print(links["href"])