"""
PythonAnywhere WSGI 설정 파일 예제
Web 탭 → WSGI configuration file에서 이 내용으로 수정하세요
"""
import os
import sys

# 프로젝트 경로 추가 (실제 사용자명으로 변경하세요)
path = '/home/yourusername/innok_django'
if path not in sys.path:
    sys.path.insert(0, path)

# 가상환경 활성화 (가상환경을 사용하는 경우)
activate_this = '/home/yourusername/innok_django/venv/bin/activate_this.py'
if os.path.exists(activate_this):
    with open(activate_this) as f:
        exec(f.read(), {'__file__': activate_this})

# Django 설정
os.environ['DJANGO_SETTINGS_MODULE'] = 'innok_site.settings_pythonanywhere'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

