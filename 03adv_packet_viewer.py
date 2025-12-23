# 간단한 네트워크 패킷 스니퍼
# 차단학고 싶은 IP 설정(ACL 규칙)
# 터미널 글자 색깔 지정
from pickle import REDUCE

from scapy.all import sniff, IP, TCP
import sys

# 터미널 색상 지정(ANCI Code)
# 이스케이프 시퀀스로 색상 지정 :ESC[코드m
#\0는 8진수, 33는 아스키코드의 27->27, 제어명령 시작을 알림
# m:색상 SGR 형식(색상 굵기 밑줄 반전)으로 표기
RED = '\033[91m' #\0는 8진수, 33는 아스키코드의 27
GREEN= '\033[92m'
RESET= '\033[0m'

# 차단하고 싶은 IP 지정(ACL)
# BLOCKED_IP = "8.8.8.8"
BLOCKED_IP = "104.18.23.5"

# 패킷이 캡쳐될 때마다 호출되는 함수
def process_packet(packet):
    # 1. IP 레이어가 있는 확인
    # 네트워크에는 IP가 없는 패킷도 존재할 수 있음 - 주의 요망!
    if packet.haslayer(IP):

        # IP 헤더에서 출발지/도착지 IP 주소 축출(프로토콜 번호도 함께)
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst


        # 2. 출발 IP가 우리가 지정한 차단 IP와 같다면

        if ip_src == BLOCKED_IP:
            print(f"{RED}" + "="*50)
            print(f"[!!!경고!!!] 차단된 IP가 감지되었습니다!!")
            print(f"{RED}" + "="*50 + f"{RESET}")
            # 정상 패킷이면
            if packet.haslayer(TCP):
                print(f"포트정보:{packet[TCP].sport}->{packet[TCP].dport}")
                print(f"{GREEN} [통과 패킷] {ip_src} -> {ip_dst} {RESET}")
        else:
            print(f"[기타 IP패킷] {ip_src}->{ip_dst}")



# 메인 실행 부분 - 프로그램의 시작점(실행 진입점)
# 현재 파이썬 파일을 직접호출했을 때만 실행되게 하고
# import 했을 때는 자동으로 실행되지 않게 하기 위한 코드

if __name__ == "__main__":
    print(">>> 패킷 감시를 시작합니다...(중지는 Ctrl+C)")

    # sniff : 패킷을 낚아채는 함수
    # filter : 낚아챌 패킷 지정
    # prn : 패킷을 잡을 때마다 호출할 함수 지정
    # store : 잡은 패킷을 메모리에 저장하지 않음(메모리 부족 방지)
    sniff(prn=process_packet, store=False)