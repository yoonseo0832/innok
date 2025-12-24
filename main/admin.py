"""
관리자 페이지 설정
"""
from django.contrib import admin
from .models import Notice, Estimate, FAQ, Newsletter


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    """공지사항 관리자"""
    list_display = ('title', 'author', 'views', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content', 'author')
    readonly_fields = ('views', 'created_at', 'updated_at')


@admin.register(Estimate)
class EstimateAdmin(admin.ModelAdmin):
    """견적문의 관리자"""
    list_display = ('title', 'author', 'category', 'company', 'phone', 'email', 'views', 'answered_at', 'created_at')
    list_filter = ('category', 'created_at', 'answered_at')
    search_fields = ('title', 'content', 'author', 'company', 'phone', 'email')
    readonly_fields = ('views', 'created_at', 'updated_at', 'answered_at')
    
    fieldsets = (
        ('문의 정보', {
            'fields': ('category', 'title', 'author', 'password', 'content')
        }),
        ('연락처 정보', {
            'fields': ('company', 'phone', 'email', 'homepage')
        }),
        ('답변 정보', {
            'fields': ('answer', 'answered_at')
        }),
        ('통계', {
            'fields': ('views', 'created_at', 'updated_at')
        }),
    )


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    """FAQ 관리자"""
    list_display = ('title', 'author', 'views', 'answered_at', 'created_at')
    list_filter = ('created_at', 'answered_at')
    search_fields = ('title', 'question', 'author')
    readonly_fields = ('views', 'created_at', 'updated_at', 'answered_at')
    
    fieldsets = (
        ('질문 정보', {
            'fields': ('title', 'author', 'password', 'question')
        }),
        ('답변 정보', {
            'fields': ('answer', 'answered_at')
        }),
        ('통계', {
            'fields': ('views', 'created_at', 'updated_at')
        }),
    )


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    """뉴스레터 관리자"""
    list_display = ('title', 'author', 'views', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content', 'author')
    readonly_fields = ('views', 'created_at', 'updated_at')
    
    fieldsets = (
        ('뉴스 정보', {
            'fields': ('title', 'author', 'image', 'content')
        }),
        ('통계', {
            'fields': ('views', 'created_at', 'updated_at')
        }),
    )
