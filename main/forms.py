"""
폼 정의
"""
from django import forms
from .models import Notice, Estimate, FAQ


class NoticeForm(forms.ModelForm):
    """공지사항 폼"""
    class Meta:
        model = Estimate
        # 모델에서 정의한 필드 순서대로 나열
        fields = [
            'category', 'title', 'author', 'company',
            'phone', 'email', 'homepage', 'password', 'content'
        ]

        widgets = {
            # 라디오 버튼 (HTML에서 렌더링 시 스타일링 필요할 수 있음)
            'category': forms.RadioSelect(attrs={'class': 'form-check-input'}),

            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '제목을 입력하세요'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '이름을 입력하세요'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '회사명을 입력하세요'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '연락처를 입력하세요 (예: 010-1234-5678)'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '이메일을 입력하세요'}),

            # 선택 항목
            'homepage': forms.URLInput(attrs={'class': 'form-control', 'placeholder': '홈페이지가 있다면 입력하세요 (선택)'}),

            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호를 입력하세요'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': '문의 내용을 상세히 적어주세요'}),
        }

        labels = {
            'category': '사업분야 (필수)',
            'author': '이름',
            'company': '회사명',
            'phone': '연락처',
            'email': '이메일',
            'homepage': '홈페이지 (URL)',
        }


class EstimateForm(forms.ModelForm):
    """견적문의 폼"""
    class Meta:
        model = Estimate
        fields = ['title', 'author', 'password', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }


class FAQForm(forms.ModelForm):
    """FAQ 폼"""
    class Meta:
        model = FAQ
        fields = ['title', 'author', 'password', 'question', 'answer']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'question': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'answer': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

