## 0429
7주차 과제
.gitignore 파일에는 .gitignore를 자동으로 생성해주는 gitignore.io 라는 사이트에서 python을 쳐서 나온 소스코드를 넣었다.
python은 3.9.11 버전을 이용하였다.


개발환경이 바뀌었을 때 일일이 패키지를 설치해줘야 한다. 
이것들을 일일이 설치하지 않고 패키지들을 기록해놓을 수 있는 명령어가 pip freeze 명령어이다.

$pip freeze > requirements.txt를 입력하면 requirements.txt파일에 출력결과를 저장 할 수 있다.
$pip install -r requirements.txt
requirements.txt에 있는 내용을 가지고 자동으로 패키지를 설치해줌으로써 해당 프로젝트가 어떤 버전의 패키지를 썼는지 기억하지 않아도 개발환경을 세팅할 수 있다. 
github 저장소에서 프로젝트를 clone한 사람도 해당 파일이 있으면 가상환경을 하나 만든 후 바로 세팅이 가능하다.
