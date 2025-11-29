# INNOK 홈페이지

의료제품 GMP 교육 및 컨설팅 전문 기업 INNOK의 공식 홈페이지입니다.

## 기술 스택

- **Backend**: Django 4.2
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript (ES6+)
- **Database**: SQLite (개발) / MySQL (프로덕션)
- **배포**: GitHub Pages (정적 파일) + Django 서버

## 프로젝트 구조

```
INNOK/
├── innok_site/          # Django 프로젝트 설정
├── main/                # 메인 앱 (공개 페이지)
│   ├── models.py        # 데이터베이스 모델
│   ├── views.py         # 뷰 함수
│   ├── urls.py          # URL 라우팅
│   └── templates/       # 템플릿 파일
├── admin_panel/         # 관리자 패널 앱
│   ├── views.py         # 관리자 뷰
│   └── templates/       # 관리자 템플릿
├── data/                # JSON 데이터 파일
│   ├── projects.json    # 사업소개 데이터
│   ├── about.json       # 회사소개 데이터
│   └── contact.json     # 고객센터 데이터
├── static/              # 정적 파일 (CSS, JS, 이미지)
├── templates/           # 기본 템플릿
└── media/               # 업로드된 파일

```

## 설치 및 실행

### 1. 가상환경 생성 및 활성화

```bash
# 가상환경 생성
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. 데이터베이스 마이그레이션

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 관리자 계정 생성

```bash
python manage.py createsuperuser
```

### 5. 개발 서버 실행

```bash
python manage.py runserver
```

서버가 실행되면 http://127.0.0.1:8000 에서 사이트를 확인할 수 있습니다.

## 관리자 접근

- **일반 관리자 페이지**: http://127.0.0.1:8000/admin/
- **커스텀 관리자 패널**: http://127.0.0.1:8000/innokadm/

## 주요 기능

### 공개 페이지
- 메인 페이지 (히어로 섹션, 슬라이더)
- 사업소개 (5가지 사업 영역)
- 회사소개
- 고객센터 (연락처, 지도)
- 공지사항 (게시판)
- 견적문의 (Q&A 게시판)
- 자주하는 질문 (FAQ)
- PR CENTER (동영상, 사진 갤러리)

### 관리자 기능
- JSON 데이터 관리 (사업소개, 회사소개, 고객센터)
- 게시판 관리 (공지사항, 견적문의, FAQ)
- 데이터 다운로드/업로드

## 데이터 관리

### JSON 데이터 파일

- `data/projects.json`: 사업소개 프로젝트 데이터
- `data/about.json`: 회사소개 데이터
- `data/contact.json`: 고객센터 정보

이 파일들은 관리자 패널에서 직접 편집할 수 있으며, JSON 형식으로 다운로드/업로드 가능합니다.

### 데이터베이스

게시판 데이터는 SQLite (개발) 또는 MySQL (프로덕션) 데이터베이스에 저장됩니다.

## 배포

### GitHub Pages 배포 (정적 사이트)

이 프로젝트는 GitHub Actions를 통해 정적 사이트로 빌드되어 GitHub Pages에 자동 배포됩니다.

**배포 활성화 방법:**
1. GitHub 저장소의 **Settings** → **Pages**로 이동
2. **Source**에서 **"GitHub Actions"** 선택
3. 저장

**배포 프로세스:**
- `main` 브랜치에 push하면 자동으로 빌드 및 배포됩니다
- `build_static.py` 스크립트가 Django 템플릿을 정적 HTML로 변환합니다
- 정적 파일(CSS, JS, 이미지)이 함께 배포됩니다
- 배포된 사이트: https://kiminsun.github.io/innok_django

**주의사항:**
- GitHub Pages는 정적 사이트만 호스팅 가능합니다
- 동적 기능(공지사항, 견적문의 등)은 Django 서버가 필요합니다
- 현재는 정적 페이지(메인, 사업소개, 회사소개, 고객센터)만 배포됩니다

### Django 서버 배포 (전체 기능)

전체 Django 기능을 사용하려면 별도의 서버가 필요합니다:

**추천 플랫폼:**
- **Railway** (https://railway.app) - 무료 티어 제공
- **Render** (https://render.com) - 무료 티어 제공
- **Heroku** (유료)
- **AWS/Azure/GCP** (프로덕션용)

**프로덕션 설정:**

프로덕션 환경에서는 다음 설정을 변경해야 합니다:

- `DEBUG = False`
- `ALLOWED_HOSTS` 설정
- `SECRET_KEY` 환경 변수로 관리
- 데이터베이스 설정 (MySQL 또는 PostgreSQL)

## 개발 가이드

### 새로운 기능 추가

1. 모델 추가: `main/models.py`
2. 뷰 추가: `main/views.py`
3. URL 추가: `main/urls.py`
4. 템플릿 추가: `main/templates/main/`

### 정적 파일 추가

정적 파일은 `static/` 디렉토리에 추가하고, 템플릿에서 `{% load static %}` 후 `{% static 'path/to/file' %}` 형식으로 사용합니다.

## 라이선스

이 프로젝트는 INNOK의 소유입니다.

## 문의

- 이메일: innogi2020@innok.kr
- 전화: 02-756-7094
