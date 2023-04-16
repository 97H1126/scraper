from requests import get

sites = ("https://google.com", 
         "https://tiktok",
         "instagram.com",
         "naver",
         "https://httpstat.us/502", #유효하지 않은 페이지 테스트
        )

ok_list={}
not_ok_list={}
# 주소 와 상태 코드 확인
for i in sites :
    if not i.startswith("https://"):
        i = f"https://{i}"

    if not i.endswith(".com"):
        i=f"{i}.com"

    print(i)
    result=get(i).status_code
    print(result)

# 상태 코드에 따른 분류 
    if result >=100 and result <200 :
        print("정보응답")
        ok_list[i] = "ok"

    elif result >= 200 and result<300 :
        print(f"{i} 상태 응답 좋음")
        ok_list[i] = "ok"

    
    elif result>= 300 and result < 400 :
        print(f"{i}상태 응답 좋지 않음")
        not_ok_list[i] = "not ok"
        

    else :
        print(f"{i}서버 상태 좋지 않음")
        not_ok_list[i] = "not ok"

print(ok_list , not_ok_list)





