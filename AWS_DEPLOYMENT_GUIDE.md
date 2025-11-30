# AWS 배포 가이드

Django 애플리케이션을 AWS에 배포하는 방법과 필요한 서비스 안내입니다.

## 🎯 추천 배포 옵션 비교

### 1. **AWS Elastic Beanstalk** ⭐ (가장 추천)

**장점:**
- 가장 간단하고 빠른 배포
- 자동 스케일링, 로드 밸런싱, 모니터링 포함
- Django에 최적화된 환경 제공
- 무료 티어 제공 (제한적)

**비용:**
- 무료 티어: 750시간/월 (t2.micro 또는 t3.micro)
- 유료: 약 $15-30/월 (t3.small 기준)

**추천 이유:**
- 초보자도 쉽게 배포 가능
- 인프라 관리 최소화
- 프로덕션 환경에 적합

---

### 2. **AWS Lightsail** 💡 (비용 효율적)

**장점:**
- 예측 가능한 저렴한 가격
- 간단한 VPS 스타일 관리
- 고정 요금제

**비용:**
- $3.50/월 (512MB RAM, 1 vCPU)
- $5/월 (1GB RAM, 1 vCPU) - **추천**
- $10/월 (2GB RAM, 1 vCPU)

**추천 이유:**
- 저렴한 비용
- 소규모 프로젝트에 적합
- 예측 가능한 비용

---

### 3. **AWS EC2** (고급 사용자용)

**장점:**
- 완전한 제어권
- 다양한 인스턴스 타입 선택
- 유연한 설정

**단점:**
- 직접 서버 관리 필요
- 보안 설정 복잡
- 초기 설정 시간 소요

**비용:**
- t2.micro: 무료 티어 (750시간/월)
- t3.small: 약 $15/월
- t3.medium: 약 $30/월

---

### 4. **AWS App Runner** (컨테이너 기반)

**장점:**
- 자동 스케일링
- 컨테이너 기반 배포
- 서버리스 스타일

**비용:**
- CPU: $0.007/vCPU-시간
- 메모리: $0.0008/GB-시간
- 약 $10-20/월 (소규모 트래픽)

---

## 📋 필요한 AWS 서비스

### 필수 서비스

1. **애플리케이션 호스팅**
   - Elastic Beanstalk (추천) 또는 Lightsail

2. **데이터베이스**
   - **RDS (MySQL/PostgreSQL)**: $15-30/월
   - 또는 **RDS Free Tier**: 750시간/월 (제한적)

3. **정적 파일 저장**
   - **S3**: $0.023/GB/월 (거의 무료)
   - **CloudFront CDN** (선택): $0.085/GB (첫 10TB)

4. **도메인 및 SSL**
   - **Route 53**: $0.50/월 (호스팅 영역)
   - **ACM (SSL 인증서)**: 무료

### 선택적 서비스

5. **이메일 발송** (견적문의 등)
   - **SES**: $0.10/1000건 (무료 티어: 62,000건/월)

6. **모니터링**
   - **CloudWatch**: 무료 티어 제공

---

## 💰 예상 비용 (월간)

### 옵션 1: Elastic Beanstalk + RDS (추천)
- Elastic Beanstalk: 무료 티어 또는 $15-30
- RDS (db.t3.micro): $15-20
- S3: $1-2
- **총계: 약 $16-52/월**

### 옵션 2: Lightsail (가장 저렴)
- Lightsail ($5 플랜): $5
- Lightsail 데이터베이스: $15
- **총계: 약 $20/월**

### 옵션 3: EC2 직접 관리
- EC2 (t3.small): $15
- RDS (db.t3.micro): $15-20
- S3: $1-2
- **총계: 약 $31-37/월**

---

## 🚀 배포 단계별 가이드

### Elastic Beanstalk 배포 (추천)

1. **EB CLI 설치**
```bash
pip install awsebcli
```

2. **EB 초기화**
```bash
eb init -p python-3.9 innok-django
```

3. **환경 변수 설정**
```bash
eb setenv SECRET_KEY=your-secret-key DEBUG=False
```

4. **배포**
```bash
eb create innok-prod
eb deploy
```

### Lightsail 배포

1. **Lightsail 인스턴스 생성**
   - AWS 콘솔 → Lightsail → 인스턴스 생성
   - OS: Ubuntu
   - 플랜: $5/월 선택

2. **SSH 접속 및 설정**
```bash
# SSH 접속
ssh -i your-key.pem ubuntu@your-instance-ip

# Django 설치 및 설정
sudo apt update
sudo apt install python3-pip python3-venv nginx
```

---

## 📝 프로덕션 설정 체크리스트

- [ ] `DEBUG = False` 설정
- [ ] `SECRET_KEY` 환경 변수로 관리
- [ ] `ALLOWED_HOSTS` 설정
- [ ] 데이터베이스 (RDS) 연결
- [ ] 정적 파일 S3 저장
- [ ] 미디어 파일 S3 저장
- [ ] SSL 인증서 설정
- [ ] 도메인 연결
- [ ] 백업 설정
- [ ] 모니터링 설정

---

## 🎯 최종 추천

**초보자 또는 빠른 배포:** AWS Elastic Beanstalk
**비용 절감:** AWS Lightsail ($5 플랜)
**완전한 제어:** AWS EC2

---

## 📚 참고 자료

- [AWS Elastic Beanstalk Django 가이드](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)
- [AWS Lightsail 가이드](https://lightsail.aws.amazon.com/)
- [Django 프로덕션 배포 체크리스트](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)

