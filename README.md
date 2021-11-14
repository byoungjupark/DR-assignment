# Task API
FastAPI 프레임워크를 사용하여 Task API 구현

## 사용 기술
<img src="https://img.shields.io/badge/Python 3.9-3776AB?style=for-the-badge&logo=Python&logoColor=white"/>&nbsp;
<img alt="Python" src = "https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/>&nbsp;
<img alt="Python" src = "https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/Docker-0052CC?style=for-the-badge&logo=Docker&logoColor=white"/>&nbsp;

## 실행 방법
#### 프로젝트 설치
해당 레파지토리를 clone하고, 다운받은 디렉토리로 들어갑니다.
```
git clone https://github.com/byoungjupark/DR-assignment.git
cd DR-assignment
```

#### 환경 구축
minicodna나 docker 환경을 구축합니다.
```
## miniconda 환경
conda create --name [프로젝트 이름] python=3.9
conda activate [프로젝트 이름]
pip install -r requirements.txt
```

```
## docker 환경
docker-compose up
```

`secrets_sample.json` 파일을 참고하여 app 디렉토리 안에 `secerets.json` 파일을 생성 후 database 환경설정을 진행합니다.
#### 서버 실행
```
uvicorn app.main:app --reload
```


## API 명세서
FastAPI에서 제공하는 Swagger로 진행하였습니다.
아래 url에서 확인하실 수 있습니다.
```
http://localhost:8000/docs
```
![api_doc](https://images.velog.io/images/byoungju1012/post/c8564532-84a4-4a0a-b305-c477c695901d/swagger.png)

## 유닛테스트
최상단 디렉토리에서 아래 명령어로 유닛테스트를 진행합니다.
```
pytest tests.tasks.py
```

![test](https://images.velog.io/images/byoungju1012/post/8fc64742-3337-4c73-a083-dfa5c0d1bdac/test.png)


## 디렉토리 구조
```
├── Dockerfile
├── app
│   ├── __init__.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── secrets.json
│   └── tasks
│       ├── __init__.py
│       ├── main.py
│       ├── models.py
│       └── schemas.py
├── docker-compose.yml
├── requirements.txt
├── secrets_sample.json
└── tests
    ├── __init__.py
    ├── database.py
    ├── secrets.json
    └── tasks.py
```
