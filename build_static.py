"""
Django 템플릿을 정적 HTML로 변환하는 스크립트
GitHub Pages 배포를 위해 사용
"""
import os
import sys
import django
from pathlib import Path

# Django 설정
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'innok_site.settings')
django.setup()

from django.template.loader import render_to_string
from django.template import Context, Template
from django.conf import settings
from django.contrib.staticfiles.finders import find
import json
import shutil
import re

# 출력 디렉토리
OUTPUT_DIR = BASE_DIR / 'dist'
STATIC_DIR = OUTPUT_DIR / 'static'

def load_json_data(filename):
    """JSON 데이터 파일 로드"""
    json_path = settings.JSON_DATA_DIR / filename
    if json_path.exists():
        with open(json_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def replace_static_paths(html, base_path='/innok_django'):
    """
    Django static 태그를 GitHub Pages 경로로 변환
    """
    # {% static 'path' %} 패턴 찾기
    def replace_static(match):
        static_path = match.group(1)
        # GitHub Pages 프로젝트 페이지는 /repository_name/ 경로 사용
        return f"{base_path}/static/{static_path}"

    # {% static '...' %} 패턴 매칭 및 교체
    pattern = r"{%\s*static\s+['\"]([^'\"]+)['\"]\s*%}"
    html = re.sub(pattern, replace_static, html)

    # url 태그도 처리
    def replace_url(match):
        url_name = match.group(1)
        # URL 매핑
        url_map = {
            'main:index': f'{base_path}/',
            'main:business': f'{base_path}/business/',
            'main:about': f'{base_path}/about/',
            'main:contact': f'{base_path}/contact/',
            'main:notice_list': f'{base_path}/notice/',
            'main:estimate_list': f'{base_path}/estimate/',
            'main:faq_list': f'{base_path}/faq/',
            'main:pr_center': f'{base_path}/pr/',
        }
        return url_map.get(url_name, f'{base_path}/')

    url_pattern = r"{%\s*url\s+['\"]([^'\"]+)['\"]\s*%}"
    html = re.sub(url_pattern, replace_url, html)

    # 절대 경로를 base_path 포함 경로로 변환
    def replace_absolute_path(match):
        quote = match.group(1)  # " 또는 '
        path = match.group(2)
        if path.startswith('/') and not path.startswith(base_path):
            # 루트 경로는 base_path로
            if path == '/':
                return f'href{quote}{base_path}/{quote}'
            return f'href{quote}{base_path}{path}{quote}'
        return match.group(0)

    # href="/..." 또는 href='...' 패턴 처리
    href_pattern = r'href=(["\'])(/[^"\']*)\1'
    html = re.sub(href_pattern, replace_absolute_path, html)

    return html

def build_static_pages():
    """정적 페이지 빌드"""
    # 출력 디렉토리 생성
    OUTPUT_DIR.mkdir(exist_ok=True)
    STATIC_DIR.mkdir(exist_ok=True)

    # JSON 데이터 로드
    projects_data = load_json_data('projects.json')
    about_data = load_json_data('about.json')
    contact_data = load_json_data('contact.json')

    # 정적 페이지 렌더링
    pages = [
        {
            'template': 'main/index.html',
            'output': 'index.html',
            'context': {}
        },
        {
            'template': 'main/business.html',
            'output': 'business/index.html',
            'context': {'projects': projects_data}
        },
        {
            'template': 'main/about.html',
            'output': 'about/index.html',
            'context': {'about': about_data}
        },
        {
            'template': 'main/contact.html',
            'output': 'contact/index.html',
            'context': {'contact': contact_data}
        },
    ]

    for page in pages:
        try:
            # 템플릿 렌더링
            html = render_to_string(page['template'], page['context'])

            # 정적 파일 경로 변환
            html = replace_static_paths(html)

            # 출력 경로 생성
            output_path = OUTPUT_DIR / page['output']
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # HTML 저장
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(html)

            print(f"✓ Built: {page['output']}")
        except Exception as e:
            print(f"✗ Error building {page['output']}: {e}")
            import traceback
            traceback.print_exc()

    # 정적 파일 복사
    if (BASE_DIR / 'static').exists():
        shutil.copytree(
            BASE_DIR / 'static',
            STATIC_DIR,
            dirs_exist_ok=True
        )
        print("✓ Copied static files")

    # collectstatic으로 수집된 파일 복사
    if (BASE_DIR / 'staticfiles').exists():
        staticfiles_dir = OUTPUT_DIR / 'staticfiles'
        shutil.copytree(
            BASE_DIR / 'staticfiles',
            staticfiles_dir,
            dirs_exist_ok=True
        )
        print("✓ Copied collected static files")

    # .nojekyll 파일 생성 (Jekyll 처리 비활성화)
    nojekyll_path = OUTPUT_DIR / '.nojekyll'
    nojekyll_path.touch()
    print("✓ Created .nojekyll file")

    # 빌드 결과 확인
    html_files = list(OUTPUT_DIR.rglob('*.html'))
    print(f"\n✓ Static site built successfully in {OUTPUT_DIR}")
    print(f"✓ Generated {len(html_files)} HTML files")
    for html_file in html_files:
        print(f"  - {html_file.relative_to(OUTPUT_DIR)}")

if __name__ == '__main__':
    build_static_pages()

