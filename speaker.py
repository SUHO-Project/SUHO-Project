import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# 음성 인식 (듣기, STT)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko')
        print('[김태기] : ' + text)
        answer(text)
    except sr.UnknownValueError:
        print('인식 실패') # 음성 인식 실패한 경우 
    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e)) # API Key 오류, 네트워크 단절 등


# 대답
def answer(input_text):
    answer_text = ''
    if '키오스크' in input_text:
        answer_text = '원하시는 교육과정을 선택해주세요'
    elif 'ATM' in input_text:
        answer_text = '예금출금 입금 무통장송금 예금조회중 원하시는 교육과정을 선택해주세요'
    elif '예금' in input_text:
        answer_text = '카드 및 통장을 넣어 주십시오'
    elif '다음' in input_text:
        answer_text = '찾으실 금액을 선택하여 주십시오'
    elif '만 원' in input_text:
        answer_text = '찾으시는 금액의 내용입니다. 거래하실 금액을 확인하시고 계속 거래를 원하시면 확인을 원하지 않으시면 취소를 눌러주십시오'
    elif '확인' in input_text:
        answer_text = '비밀번호 4자리를 눌러주십시오'
    elif '입력' in input_text:
        answer_text = '현금을 수령해주세요 현금 수령 시 개폐기가 자동으로 닫힙니다.'
    elif '종료' in input_text:
        answer_text = '다음에 또 만나요'
        stop_listening(wait_for_stop=False) # 더 이상 듣지 않음 
    else:
        answer_text = '다시 한 번 말씀해주시겠어요?'
    speak(answer_text)

# 소리내어 일기(TTS)
def speak(text):
    print('[인공지능] : ' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name): # voice.mp3 파일 삭제
        os.remove(file_name)

r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
# 사람처럼 귀가 열려있음 백그라운드에서 듣고있다가 어떤 음성이 들어오면 처리하는 형식
stop_listening = r.listen_in_background(m, listen)
# stop_listening(wait_for_stop=False) # 더 이상 듣지 않음 

while True:
    time.sleep(0.1)

