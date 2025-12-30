import subprocess
import sys

def run_streamlit(appName):
    #터미널 : streamlit run 11streamlit_subprocess.py
    #(가상환경에서 지원하는) 파이썬으로 실행 : python -m streamlit run 11streamlit_subprocess.py
    #subprocess : python으로 외부 프로세스를 실행 제어하는 도구
    subprocess.run([sys.executable,
                    "-m", "streamlit", "run", str(appName)])

# 실행 진입점
# 위치는 파일 맨 아래
if __name__=="__main__":
    # run_streamlit()를 직접 호출하면 문제 발생 - 자기 자신을 계속 호출
    # run_streamlit()
    # run_streamlit("12streamlit_tab.py")
    # run_streamlit("13streamlit_multi_pages.py")
    # run_streamlit("14streamlit_multi_pages.py")
    run_streamlit("15streamlit_query_params.py")