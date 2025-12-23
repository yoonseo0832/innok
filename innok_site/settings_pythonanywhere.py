"""
PythonAnywhere 프로덕션 환경 설정 파일
"""
from .settings import *
import os

# 보안 설정
DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'change-this-secret-key-in-production')

# 허용된 호스트 설정 (PythonAnywhere 사용자명으로 변경 필요)
ALLOWED_HOSTS = [
    'innok.kr',           # 이 줄 추가!
    'www.innok.kr',
    'yoonseo03.pythonanywhere.com',  # 실제 사용자명으로 변경하세요
]

# 정적 파일 설정
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 데이터베이스 (SQLite 사용 - 무료 계정)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 보안 헤더 (HTTPS 사용 시)
# PythonAnywhere 무료 계정은 HTTPS를 지원하지 않으므로 주석 처리
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# 로깅 설정
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django.log'),
            'formatter': 'verbose',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'root': {
        'handlers': ['console', 'file'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

