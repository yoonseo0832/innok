// 메인 JavaScript 파일

// DOM 로드 완료 시 실행
document.addEventListener('DOMContentLoaded', function() {
    initNavigation();
    initScrollAnimations();
    initSmoothScroll();
});

// 네비게이션 바 스크롤 효과
function initNavigation() {
    const navbar = document.getElementById('mainNav');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });
}

// 스크롤 애니메이션 초기화
function initScrollAnimations() {
    // AOS 초기화
    if (typeof AOS !== 'undefined') {
        AOS.init({
            duration: 1000,
            once: true,
            offset: 100
        });
    }
    
    // 커스텀 페이드인 애니메이션
    const fadeElements = document.querySelectorAll('.fade-in');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            }
        });
    }, {
        threshold: 0.1
    });
    
    fadeElements.forEach(el => observer.observe(el));
}

// 부드러운 스크롤
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const href = this.getAttribute('href');
            if (href === '#') return; // 빈 링크 무시
            
            const target = document.querySelector(href);
            
            if (target) {
                // 모바일 메뉴 닫기
                const navbarCollapse = document.getElementById('navbarNav');
                if (navbarCollapse) {
                    // Bootstrap Collapse API 사용 시도
                    if (typeof bootstrap !== 'undefined' && bootstrap.Collapse) {
                        const bsCollapse = bootstrap.Collapse.getInstance(navbarCollapse);
                        if (bsCollapse) {
                            bsCollapse.hide();
                        } else if (navbarCollapse.classList.contains('show')) {
                            const newCollapse = new bootstrap.Collapse(navbarCollapse, {
                                toggle: false
                            });
                            newCollapse.hide();
                        }
                    } else {
                        // Bootstrap이 없는 경우 직접 클래스 제거
                        navbarCollapse.classList.remove('show');
                        const toggler = document.querySelector('[data-bs-toggle="collapse"]');
                        if (toggler) {
                            toggler.setAttribute('aria-expanded', 'false');
                        }
                    }
                }
                
                // 약간의 딜레이 후 스크롤 (메뉴가 닫히는 시간 고려)
                setTimeout(function() {
                    const navbarHeight = document.getElementById('mainNav').offsetHeight;
                    const targetPosition = target.offsetTop - navbarHeight;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                }, 100);
            }
        });
    });
}

// 현재 섹션 하이라이트
window.addEventListener('scroll', function() {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-link[href^="#"]');
    
    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop;
        const sectionHeight = section.clientHeight;
        if (window.scrollY >= (sectionTop - 200)) {
            current = section.getAttribute('id');
        }
    });
    
    navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + current) {
            link.classList.add('active');
        }
    });
});

// 로딩 애니메이션
function showLoading() {
    const loader = document.createElement('div');
    loader.className = 'loading';
    loader.innerHTML = '<div class="spinner"></div>';
    document.body.appendChild(loader);
}

function hideLoading() {
    const loader = document.querySelector('.loading');
    if (loader) {
        loader.remove();
    }
}

// 이미지 레이지 로딩
if ('loading' in HTMLImageElement.prototype) {
    const images = document.querySelectorAll('img[loading="lazy"]');
    images.forEach(img => {
        img.src = img.dataset.src;
    });
} else {
    // 레이지 로딩 폴리필
    const script = document.createElement('script');
    script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.3.2/lazysizes.min.js';
    document.body.appendChild(script);
}

