"""
메인 뷰 함수
"""
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Notice, Estimate, FAQ, Newsletter
import json
import os
from django.conf import settings


def index(request):
    """메인 페이지"""
    return render(request, 'main/index.html')


def business(request):
    """사업소개 페이지"""
    # JSON 형식 요청 처리
    if request.GET.get('format') == 'json':
        from django.http import JsonResponse
        json_path = settings.JSON_DATA_DIR / 'projects.json'
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 특정 프로젝트 상세 정보 요청
            project_id = request.GET.get('id')
            project_type = request.GET.get('type')
            if project_id and project_type:
                projects = data.get(project_type, [])
                project = next((p for p in projects if p.get('id') == int(project_id)), None)
                if project:
                    return JsonResponse(project)
                return JsonResponse({'error': 'Project not found'}, status=404)
            
            return JsonResponse(data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return render(request, 'main/business.html')


def about(request):
    """회사소개 페이지"""
    return render(request, 'main/about.html')


def contact(request):
    """고객센터 페이지"""
    return render(request, 'main/contact.html')


def notice_list(request):
    """공지사항 목록"""
    notices = Notice.objects.all()
    
    # 검색 기능
    search_query = request.GET.get('search', '')
    if search_query:
        notices = notices.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query) |
            Q(author__icontains=search_query)
        )
    
    # 페이지네이션
    paginator = Paginator(notices, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'main/notice_list.html', context)


def notice_detail(request, pk):
    """공지사항 상세보기"""
    notice = Notice.objects.get(pk=pk)
    notice.views += 1
    notice.save()
    return render(request, 'main/notice_detail.html', {'notice': notice})


def estimate_list(request):
    """견적문의 목록"""
    estimates = Estimate.objects.all()
    
    # 검색 기능
    search_query = request.GET.get('search', '')
    if search_query:
        estimates = estimates.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query) |
            Q(author__icontains=search_query)
        )
    
    # 페이지네이션
    paginator = Paginator(estimates, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'main/estimate_list.html', context)


def estimate_create(request):
    """견적문의 작성"""
    from .forms import EstimateForm
    
    if request.method == 'POST':
        form = EstimateForm(request.POST)
        if form.is_valid():
            estimate = form.save()
            return redirect('main:estimate_detail', pk=estimate.pk)
    else:
        form = EstimateForm()
    
    return render(request, 'main/estimate_create.html', {'form': form})


def estimate_detail(request, pk):
    """견적문의 상세보기"""
    try:
        estimate = Estimate.objects.get(pk=pk)
    except Estimate.DoesNotExist:
        return redirect('main:estimate_list')
    
    # 비밀번호 확인
    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password == estimate.password:
            estimate.views += 1
            estimate.save()
            return render(request, 'main/estimate_detail.html', {'estimate': estimate})
        else:
            error_message = '비밀번호가 올바르지 않습니다.'
            return render(request, 'main/estimate_detail.html', 
                         {'estimate': estimate, 'error_message': error_message})
    
    return render(request, 'main/estimate_detail.html', {'estimate': estimate})


def faq_list(request):
    """FAQ 목록"""
    faqs = FAQ.objects.all()
    
    # 검색 기능
    search_query = request.GET.get('search', '')
    if search_query:
        faqs = faqs.filter(
            Q(title__icontains=search_query) | 
            Q(question__icontains=search_query) |
            Q(author__icontains=search_query)
        )
    
    # 페이지네이션
    paginator = Paginator(faqs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'main/faq_list.html', context)


def faq_detail(request, pk):
    """FAQ 상세보기"""
    faq = FAQ.objects.get(pk=pk)
    
    # 비밀번호 확인
    if request.method == 'POST':
        password = request.POST.get('password', '')
        if password == faq.password:
            faq.views += 1
            faq.save()
            return render(request, 'main/faq_detail.html', {'faq': faq})
        else:
            error_message = '비밀번호가 올바르지 않습니다.'
            return render(request, 'main/faq_detail.html', 
                         {'faq': faq, 'error_message': error_message})
    
    return render(request, 'main/faq_detail.html', {'faq': faq})


def pr_center(request):
    """PR CENTER 페이지"""
    return render(request, 'main/pr_center.html')


def newsletter_list(request):
    """뉴스레터 목록"""
    newsletters = Newsletter.objects.all()
    
    # 검색 기능
    search_query = request.GET.get('search', '')
    if search_query:
        newsletters = newsletters.filter(
            Q(title__icontains=search_query) | 
            Q(content__icontains=search_query) |
            Q(author__icontains=search_query)
        )
    
    # 페이지네이션
    paginator = Paginator(newsletters, 16)  # 4x4 = 16개
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'main/newsletter_list.html', context)


def newsletter_detail(request, pk):
    """뉴스레터 상세보기"""
    try:
        newsletter = Newsletter.objects.get(pk=pk)
        newsletter.views += 1
        newsletter.save()
    except Newsletter.DoesNotExist:
        return redirect('main:newsletter_list')
    
    # 카카오톡 공유를 위한 URL 생성
    share_url = request.build_absolute_uri(request.path)
    
    # 카카오 JavaScript Key 가져오기 (settings에서)
    kakao_key = getattr(settings, 'KAKAO_JAVASCRIPT_KEY', None)
    
    context = {
        'newsletter': newsletter,
        'share_url': share_url,
        'KAKAO_JAVASCRIPT_KEY': kakao_key,
    }
    return render(request, 'main/newsletter_detail.html', context)
