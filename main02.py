# main01에서 만든 함수를 가져다쓰는 방법이고 여기에 필요한 툴들을 import 해준다
from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_job # extractor파일안에 있는 wwr파일에서 extract_job함수를 불러와서 사용하겠다는 의미


# job = extract_wwr_job("python") #함수를 호출한다
# print(job)