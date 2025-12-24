import streamlit as st
import pandas as pd
from scapy.all import sniff,IP,TCP, ICMP, send
from datetime import datetime

st.title("Hello,Scapy!!")

# 패킷 5개 캡처 후 출력
# 캡처한 패킷은 streamlit 콘솔에 출력
# sniff(count = 5, prn=lambda x: print(x))
packets = sniff(count = 5)
for p in packets:
    # st.text(p)
    st.write(p)

st.markdown("### tcp 패킷 5개 캡처 후 출력")
# 특정 프로토콜만 캡쳐
packets = sniff(filter="tcp",count = 5)
for p in packets:
    # print(p)
    # st.text(p)
    st.write(p)

# ICMP 패킷 하나 생성하고 전송
st.markdown("### ICMP 패킷 하나 생성하고 전송")
packet = IP(dst ="8.8.8.8") /ICMP()
for _ in range(1):
    send(packet,verbose=0) # verbose=0는 결과 없으면 보내지마
    st.success("Sent 1 packet")

# 패킷 구조 확인
st.markdown("### 패킷 구조 확인 ")
st.text(packet.show(dump=True)) # dump를 처리할 수 있는 곳으로 넘겨라

# 패킷캡처후 데이터프레임으로 출력
html_page = """
<div style="background-color:orange; padding:20px">
<p style="color:white; font-size:20px">패킷 구조 확인</p>
</div>
"""
st.markdown(html_page, unsafe_allow_html=True)

packets = sniff(filter="tcp",count = 5)
# for p in packets:
#     st.text(p.time) # 타임스탬프 형식
#     st.text(p[0].src)
#     st.text(p[0].dst)
#     st.text(p[0].summary())
data = []
for p in packets:
    # data.append({
    #     "Time":p.time,
    #     "Source":p[0].src if hasattr(p[0],"src") else "",
    #     "Destination":p[0].dst if hasattr(p[0],"dst") else ""
    # })
    data.append({
        "Time":datetime.fromtimestamp(p.time).strftime('%Y-%m-%d %H:%M:%S'),
        "Src MAC":p[0].src if hasattr(p[0],"src") else "",
        "Dst MAC":p[0].dst if hasattr(p[0],"dst") else "",
        "Src IP":p[IP].src if hasattr(p[IP],"src") else "",
        "Dst IP":p[IP].dst if hasattr(p[IP],"dst") else "",
        "Src PORT":p[TCP].sport if hasattr(p[TCP],"sport") else "",
        "Dst PORT":p[TCP].dport if hasattr(p[TCP],"dport") else ""
})

df = pd.DataFrame(data)
st.dataframe(df)

# 버튼 클릭시 패킷 캡처 시작

st.markdown("### tcp 패킷 5개 캡처 후 출력")
if st.button("🔘"):
    packets = sniff(filter="tcp",count = 5)
    for p in packets:
        # print(p)
        # st.text(p)
        st.write(p)

