from requests import get

# 웹사이트 https:// 안붙어있는거 고쳐서 출력해보기

#get() 함수는 requests 모듈에서 제공하는 HTTP 요청 메서드 중 하나로, 인자로 전달된 URL에 GET 요청을 보내고, 해당 요청에 대한 HTTP 응답 객체를 반환합니다.
#즉, get() 함수는 인터넷에서 데이터를 가져오는 기능을 합니다. 이 함수는 HTTP GET 메서드를 사용하여 원하는 웹페이지에 요청을 보내고, 해당 페이지의 내용을 가져와서 응답 객체로 반환
    

websites = (
    "https://naver.com",
    "https://google.com",
    "tiktok.com",
    "instagram.com"

)

status = {}

for website in websites:
    if not website.startswith("https://"):
        website=f"https://{website}"
    #print(website) # 웹사이트 https:// 안붙어있는거 고쳐서 출력
    result = get(website) 
 
    #print(result.status_code) # .status_code 결과의 상태코드만 보여주는 것
    if result.status_code == 200:
        
        print(f"{website} is ok")
        status[website] = "OK"
    
    else :
        print( f"{website} is not ok")
        status[website] = "Not OK"
print(status)