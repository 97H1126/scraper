from requests import get

base_url = "https://weworkremotely.com/remote-jobs/search?="
search_term = "python"
response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("웹사이트의 데이터를 받아 올 수 없음") 
else :print(response.text)