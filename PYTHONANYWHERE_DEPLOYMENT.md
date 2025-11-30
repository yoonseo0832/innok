# PythonAnywhere 배포 가이드

## 배포 가능 여부
✅ **배포 가능합니다!**
- PythonAnywhere는 Django를 지원합니다
- Python 3.8, 3.9, 3.10을 지원합니다
- 현재 프로젝트는 Python 3.8과 호환됩니다

## 배포 단계

### 1. PythonAnywhere 계정 생성
1. https://www.pythonanywhere.com/ 에서 계정 생성
2. 무료 계정으로 시작 가능 (제한사항 있음)
3. 유료 계정: $5/월부터 (도메인 연결, 더 많은 트래픽)

### 2. 파일 업로드
**방법 1: Git 사용 (권장)**
```bash
# PythonAnywhere 콘솔에서
cd ~
git clone https://github.com/kiminsun/innok_django.git
cd innok_django
```

**방법 2: 웹 인터페이스 사용**
- Files 탭에서 파일 업로드
- 또는 SFTP 사용 (유료 계정)

### 3. 가상환경 생성 및 의존성 설치
```bash
# PythonAnywhere 콘솔에서
cd ~/innok_django
python3.8 -m venv venv
source venv/bin/activate
pip install --user -r requirements.txt
```

### 4. 데이터베이스 마이그레이션
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. 정적 파일 수집
```bash
python manage.py collectstatic --noinput
```

### 6. WSGI 설정
**Web 탭 → WSGI configuration file** 클릭

다음 내용으로 수정:
```python
import os
import sys

# 프로젝트 경로 추가
path = '/home/yourusername/innok_django'
if path not in sys.path:
    sys.path.insert(0, path)

# 가상환경 활성화
activate_this = '/home/yourusername/innok_django/venv/bin/activate_this.py'
with open(activate_this) as f:
    exec(f.read(), {'__file__': activate_this})

# Django 설정
os.environ['DJANGO_SETTINGS_MODULE'] = 'innok_site.settings_production'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**주의:** `yourusername`을 실제 PythonAnywhere 사용자명으로 변경하세요!

### 7. 정적 파일 설정
**Web 탭 → Static files** 섹션에서:
- **URL**: `/static/`
- **Directory**: `/home/yourusername/innok_django/staticfiles`

- **URL**: `/media/`
- **Directory**: `/home/yourusername/innok_django/media`

### 8. 프로덕션 설정 파일 생성
`innok_site/settings_production.py` 파일이 필요합니다 (아래 참조)

### 9. ALLOWED_HOSTS 설정
`settings_production.py`에서:
```python
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']
```

### 10. 웹앱 재로드
**Web 탭 → Reload** 버튼 클릭

## 프로덕션 설정 파일

`innok_site/settings_production.py` 파일을 생성해야 합니다:

```python
from .settings import *
import os

# 보안 설정
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# 호스트 설정
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com']

# 정적 파일
STATIC_ROOT = '/home/yourusername/innok_django/staticfiles'
MEDIA_ROOT = '/home/yourusername/innok_django/media'

# 데이터베이스 (SQLite 사용)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

## 환경 변수 설정 (선택사항)

**Files 탭 → .env 파일 생성:**
```
SECRET_KEY=your-secret-key-here
DEBUG=False
```

## 주의사항

1. **SECRET_KEY**: 프로덕션에서는 환경 변수로 관리하거나 안전한 키를 사용하세요
2. **DEBUG**: 프로덕션에서는 반드시 `False`로 설정
3. **ALLOWED_HOSTS**: 실제 도메인으로 설정
4. **정적 파일**: `collectstatic` 실행 후 경로 확인
5. **데이터베이스**: SQLite는 무료 계정에서 사용 가능하지만, 유료 계정에서는 MySQL 권장

## 무료 계정 제한사항

- 외부 웹사이트 접근 제한 (하루 1시간)
- CPU 시간 제한
- 도메인 연결 불가 (`yourusername.pythonanywhere.com`만 사용)
- 트래픽 제한

## 문제 해결

### 정적 파일이 로드되지 않는 경우
- `collectstatic` 실행 확인
- Web 탭의 Static files 설정 확인
- 브라우저 캐시 삭제

### 500 에러 발생
- **Web 탭 → Error log** 확인
- `DEBUG = True`로 임시 변경하여 상세 오류 확인
- WSGI 설정 파일 경로 확인

### 데이터베이스 오류
- 마이그레이션 실행 확인
- 데이터베이스 파일 권한 확인

## 유용한 명령어

```bash
# 로그 확인
tail -f /var/log/yourusername.pythonanywhere.com.error.log

# Django 쉘 실행
python manage.py shell

# 관리자 계정 생성
python manage.py createsuperuser
```

## 참고 자료

- PythonAnywhere Django 배포 가이드: https://help.pythonanywhere.com/pages/DeployExistingDjangoProject
- PythonAnywhere 문서: https://help.pythonanywhere.com/

