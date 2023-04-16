from flask import Flask,render_template  #render_template 함수는 웹 어플리케이션에서 사용할 HTML 파일을 렌더링하여, 클라이언트(웹 브라우저)에게 보여줍니다.  Flask에서 제공하는 함수 중 하나

app = Flask("JobScrapper")
# app.run("0.0.0.0")

#유저가 홈페이지로 접속하면 페이지를 보여주게 하는것
@app.route("/") # 이부분은 무조건 함수 바로 위에 있어야한다!! @ = 데코레이터 를 이용하여 라우팅 경로를 설정하고 .route를 사용하여 경로를 처리하는 함수를 등록한다. "/"는 루트 경로를 의미하며 즉 웹 어플리케이션의 홈 페이지를 나타낸다
def home():
    return render_template("home.html", name="최호민") # templates폴더 안에 있는 html파일 이름을 넣는다 , name 변수를 왼쪽에 있는 home.html 에 넘겨준다 그럼 그파일 안에서 같은 이름의 변수(name)에 넣는다. 
# 위의 방식을 통해서 페이지에 들어온 유저에게 보여주는데 이것을 렌더링이라고 한다.

@app.route("/검색") #127.0.0.1:5000/hello로 검색하면 이동한다
def hello():
    return render_template("search.html")
app.run("127.0.0.1") #.run은 로컬서버를 실행시키며 사용할 서버의 주소를 넣어준다. #http 창에서 127.0.0.1:5000을 검색하면 유저 홈페이지를 볼 수 있음