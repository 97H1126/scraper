from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_job
from extractors.file import save_to_file

keyword = input("어떤 직업을 찾고 계시나요?")
indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_job(keyword)
jobs = indeed + wwr

save_to_file(keyword, jobs)


# file.py를 이용해서 크롤링해오기 완성 
#플라스크를 써보기 전 연습단계