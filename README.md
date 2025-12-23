### 우분투에서 실행하기
+ 가상환경 생성
```bash
    mkdir ~/projectACL
    cd ~/projectACL
    sudo apt update
    # 우분투에는 파이선이 최소로 깔렸기 때문에 venv와 pip 설치
    sudo apt install -y python3.10-venv python3-pip
    python3 -m venv py310b
    source py310b/bin/activate

+ scapy 패키지 설치
```bash
    # 관리자 영역에 패키지 설치
    pip install scapy
    sudo python3 -m pip install scapy

+ 메인 애플리케이션
```bash
    sudo vi ~/projectACL/main.py
    # 관리자로 실행
    sudo python3 main.py
    
### 우분투에서 미니콘다 설치하기
+ 우분투에 파이썬을 설치하는 것은 다소 번거로움
+ 왜냐하면 소스를 내려받아 직접 컴파일해야하기 때문
+ 그래서 미니콘다

mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-py311_25.11.1-1-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh

### 설치확인
```bash
# 셀 설정파일을 편집기로 열기
vi ~/.bashrc

# 맨 마지막 줄에 다음 내용 추가(miniconda3/bin 들어가는 설정 필요)
export PATH="$HOME/miniconda3/bin:$PATH"

# 변겅사항 시스템에 적용
source ~/.bashrc

# 콘바 버전 확인
conda --version

# 콘다 자동 base 환경 비활성화하고 
conda config --set auto_activate_base false
conda config --show auto_activate

```