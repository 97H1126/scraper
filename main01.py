#웹 스크래퍼 
from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "java"
response = get(f"{base_url}{search_term}")

# print(response)

if response.status_code != 200: #status_code 는 서버의 응답 상태 코드를 확인하게 해주는 메소드
    print("웹사이트의 데이터를 받아 올 수 없음") 
else :
    result=[]
    # print(response.text) # .text로 html을 불러오는지 확인해봄
    soup =BeautifulSoup(response.text,"html.parser") 
    # (1.받아온 html자체, 2.html문자열추출) 2번은 뷰티풀 수프를 이용하여 html.parser은 HTML 문서를 파싱하여 HTML 태그와 태그 사이의 텍스트 등의 정보를 추출할 수 있도록 도와준다 'html.parser' 기억하자(고정값인거 같음)
    jobs=soup.find_all("section",class_='jobs') # .find_all로 원하는 부분을 찾아낸다/클래스명으로 찾아내는것 > (태그이름, 클래스명) class_= 부분 언더바 잊으면 안됨 class는 파이썬 고유 지정 언어니까 class_로 설정한다)
    # print(len(jobs))

    for job_section in jobs : 
        job_post = job_section.find_all('li') # 모든 li들을 찾아냄 /job_post는 list의 li들이다
        job_post.pop(-1) # job 리스트만 불러오기 위해서 마지막 li인 버튼 부분을 인덱스 설정하고 지우기 위해서 .pop를 사용한다.
        for post in job_post:
            # print(post)
            # print("///////////////////////////")
            # print("")
            anchors = post.find_all('a') #주소를 가져오기 위해서 a 부분을 찾고 저장
            anchor = anchors[1] # a 부분이 두개를 가져오는데 두번째꺼가 주소니까 인덱스로 두번째꺼만 출력하고 저장
            #print(anchor['href']) #파이썬을 딕셔너리처럼 쓸수 있어서 이렇게 가져올 수 있다
            link = anchor['href'] # 뷰티풀스프는 딕셔너리 형태로 불러올 수 있고 불러 온것은 사이트 주소이다 이것을 link에 저장한다
            company, time, region = anchor.find_all('span',class_="company") # a 부분에서 불러온것을 anchor에 저장했는데 거기서 다시 회사 주소,근무시간, 지역이 company클래스랑 태그로 호출하고 순서대로 저장한다. html에서 이 순서대로 만들어져 있음
            # print(company, time, region)
            title = anchor.find('span',class_='title') #title 만 가져오기 위해서 작성했음 // 뷰티풀 스프에서 find와 find_all의 차이점은 find는 결과만 가져오고 find_all은 불러온 데이터를 리스트 형태로 가져온다는 차이점이 있다
            print(company.string, time.string, region.string, title.string) # .string을 하는 이유는 html을 없애주기 위해서 이다
            # print("//////////////////////////////")
            # print("")
            job_data = {
                "link":f"https://weworkremotely.com{link}",
                "company": company.string ,
                "time": time.string , 
                "region": region.string , 
                "title": title.string 
            }
            #job_data에 html을 뺀 데이터를 딕셔너리 형태로 만들어서 저장해준다
            result.append(job_data) #job_data는 포문에 의해 계속생겨나고 기존에 있던 데이터들은 없어지기 때문에 포문 밖에 만들어둔 result라는 리스트에 저장해놓는다.
            for a in result:
                print(a)
                print("//////////")




#5.7 Job Extraction (11:14)