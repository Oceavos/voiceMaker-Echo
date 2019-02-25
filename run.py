import os
import sys
from gtts import gTTS
import pygame
import os.path


firstUsingFile = './c7m3aas.mp3'


def first_step():
    if os.path.isfile(firstUsingFile):
        pass
    else:
        text = "안녕하세요. 목소리를 만들어주는 에코 라고 합니다. 무엇을 도와드릴까요?"
        make_first_voice = gTTS(text=text, lang='ko')
        make_first_voice.save("c7m3aas.mp3")


class getVoice():
    def __init__(self, getText, getFileName):
        self.Text = getText
        self.Fname = getFileName

    def run_make_mp3(self):
        text = self.Text
        voice = gTTS(text=text, lang='ko')
        voice.save(self.Fname + ".mp3")


def informAI():
    freq = 24000
    bitsize = -16
    channels = 1
    buffer = 2048

    pygame.mixer.init(freq, bitsize, channels, buffer)
    pygame.mixer.music.load(firstUsingFile)
    pygame.mixer.music.play()


while True:

    print('''
    1. 음성파일 만들기
    2. 음성파일 만들고 재생하기
    3. 프로그램 종료
   ''')

    first_step()
    informAI()  # PROGRAM INFORMATION

    select = int(input("무엇을 하시겠습니까? : "))

    # exit
    if select == 3:
        sys.exit()


    elif select == 1:
        getWantVoiceText = input("음성을 만들고자 하는 문장을 입력해주십시오. : ")
        getWantFileName = input("만들고자 하는 음성 파일의 이름을 입력해주십시오. : ")

        CHECK_FILE_NAME = len(getWantFileName)
        if CHECK_FILE_NAME <= 1:
            print("파일 이름은 2글자 이상으로 지정해주십시오.")
        else :
            loadClass = getVoice(getWantFileName, getWantFileName)
            loadClass.run_make_mp3()


    elif select == 2:
        getWantVoiceText_2 = input("음성을 만들고자 하는 문장을 입력해주십시오. : ")
        getWantFileName_2 = input("만들고자 하는 음성 파일의 이름을 입력해주십시오. : ")
        getClass = getVoice(getWantVoiceText_2, getWantFileName_2)
        getClass.run_make_mp3()

        '''
        Play
        '''
        freq = 24000
        bitsize = -16
        channels = 1
        buffer = 2048

        pygame.mixer.init(freq, bitsize, channels, buffer)
        pygame.mixer.music.load(getWantFileName_2 + '.mp3')
        pygame.mixer.music.play()
