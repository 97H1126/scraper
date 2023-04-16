from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_job


keyword = input("어떤 분야의 직업을 찾고 있나요?") #사용자로 부터 키워드를 입력받음


indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_job(keyword)

jobs = indeed + wwr

# for job in jobs:
#     print(job)
#     print("//////////\n///////////")


file =open(f"{keyword}.csv","w",encoding="utf-8")
file.write("직무,회사,위치,URL\n,")

for job in jobs:
    file.write(f"{job['직무']},{job['회사']},{job['위치']},{job['회사 공고 url']}\n")
file.close()


#여기까지가 웹 스크래퍼