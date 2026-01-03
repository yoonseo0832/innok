// 메인 JavaScript 파일

// DOM 로드 완료 시 실행
document.addEventListener('DOMContentLoaded', function() {
    initNavigation();
    initScrollAnimations();
    initSmoothScroll();
    initDropdownHover();
    initBusinessReveal();
});

// 네비게이션 바 스크롤 효과 (항상 보이는 헤더)
function initNavigation() {
    const navbar = document.getElementById('mainNav');
    if (!navbar) return;
    
    // 네비게이션 바가 항상 보이도록 강제 설정
    function forceNavbarVisible() {
        navbar.style.setProperty('display', 'block', 'important');
        navbar.style.setProperty('visibility', 'visible', 'important');
        navbar.style.setProperty('opacity', '1', 'important');
        navbar.style.setProperty('position', 'fixed', 'important');
        navbar.style.setProperty('top', '0', 'important');
        navbar.style.setProperty('left', '0', 'important');
        navbar.style.setProperty('right', '0', 'important');
        navbar.style.setProperty('width', '100%', 'important');
        navbar.style.setProperty('z-index', '9999', 'important');
        navbar.style.setProperty('background', '#ffffff', 'important');
        navbar.style.setProperty('transform', 'translateY(0)', 'important');
    }
    
    // 초기 상태 확인 (페이지 로드 시 스크롤 위치가 0이 아닐 수 있음)
    function updateNavbar() {
        // 네비게이션 바가 항상 보이도록 강제 보장
        forceNavbarVisible();
        
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    }
    
    // 즉시 실행
    forceNavbarVisible();
    updateNavbar();
    
    // 스크롤 이벤트 리스너 (throttle 적용하여 성능 최적화)
    let ticking = false;
    window.addEventListener('scroll', function() {
        if (!ticking) {
            window.requestAnimationFrame(function() {
                updateNavbar();
                ticking = false;
            });
            ticking = true;
        }
    });
    
    // 페이지 로드 시에도 실행
    window.addEventListener('load', function() {
        forceNavbarVisible();
        updateNavbar();
    });
    
    // DOMContentLoaded 시에도 실행
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            forceNavbarVisible();
            updateNavbar();
        });
    } else {
        forceNavbarVisible();
        updateNavbar();
    }
    
    // MutationObserver로 스타일 변경 감지 및 복구
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'attributes' && mutation.attributeName === 'style') {
                // 스타일이 변경되면 다시 강제로 보이게 설정
                setTimeout(forceNavbarVisible, 0);
            }
        });
    });
    
    observer.observe(navbar, {
        attributes: true,
        attributeFilter: ['style', 'class']
    });
    
    // 주기적으로 확인 (안전장치)
    setInterval(function() {
        if (navbar.style.display === 'none' || navbar.style.visibility === 'hidden' || navbar.style.opacity === '0') {
            forceNavbarVisible();
        }
    }, 100);
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

// 드롭다운 hover 트리거 (공지 및 뉴스 메뉴)
function initDropdownHover() {
    const dropdownItem = document.getElementById('noticeNewsDropdownItem');
    if (!dropdownItem) return;
    
    const dropdownToggle = document.getElementById('noticeNewsDropdown');
    const dropdownMenu = dropdownItem.querySelector('.dropdown-menu');
    
    if (!dropdownToggle || !dropdownMenu) return;
    
    // Hover 시 드롭다운 열기
    dropdownItem.addEventListener('mouseenter', function() {
        if (typeof bootstrap !== 'undefined' && bootstrap.Dropdown) {
            const bsDropdown = bootstrap.Dropdown.getInstance(dropdownToggle);
            if (!bsDropdown) {
                new bootstrap.Dropdown(dropdownToggle).show();
            } else {
                bsDropdown.show();
            }
        } else {
            dropdownMenu.classList.add('show');
            dropdownToggle.setAttribute('aria-expanded', 'true');
        }
    });
    
    // 마우스가 떠날 때 드롭다운 닫기 (약간의 딜레이)
    let hoverTimeout;
    dropdownItem.addEventListener('mouseleave', function() {
        hoverTimeout = setTimeout(function() {
            if (typeof bootstrap !== 'undefined' && bootstrap.Dropdown) {
                const bsDropdown = bootstrap.Dropdown.getInstance(dropdownToggle);
                if (bsDropdown) {
                    bsDropdown.hide();
                }
            } else {
                dropdownMenu.classList.remove('show');
                dropdownToggle.setAttribute('aria-expanded', 'false');
            }
        }, 200);
    });
    
    // 드롭다운 메뉴에 마우스가 있으면 닫지 않음
    dropdownMenu.addEventListener('mouseenter', function() {
        clearTimeout(hoverTimeout);
    });
}

// Business 페이지 스크롤 등장 효과 (Intersection Observer API)
function initBusinessReveal() {
    const revealElements = document.querySelectorAll('.reveal');
    if (revealElements.length === 0) return;
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // 한 번만 실행되도록 옵저버 해제
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    revealElements.forEach(element => {
        observer.observe(element);
    });
}

