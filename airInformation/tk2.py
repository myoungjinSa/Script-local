# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import urllib.request
import xml.etree.ElementTree as etree
import webbrowser
import noti


menu ={'0':'시간별 국제선','1':'시간별 국내선','2':'공항별 국내선','3':'종합 날씨 조회','4':'면세점 시설 검색','5':'비면세점 시설 검색','6':'인천공항 지도 사이트 연결','7':'이메일 전송','8':'c++연동'}

key = 'QydOrzDVYNDcxRwTCTjElQ8FWVC7fQgJ8JVlglIlMmFtva3gU65%2BRmV%2FlyxorjQzmRAiXGxM%2F2E1PXAC56NWdg%3D%3D'

startTime =0.0
endTime =0.0

window = Tk()



def TopText():
    MainText = Label(window ,fg='blue',text=" 항공정보 APP ", font = 'helvetica 31')
    MainText.place(x=340)

def InitRenderText():
    global RenderText
    global window

    RenderTextScrollbar = Scrollbar(window)
    RenderTextScrollbar.place(x=796, y=280)

    RenderText = Text(window, width=80, height=30, bd=3, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.place(x=197, y=276)
    RenderTextScrollbar.config(command=RenderText.yview)

def MainSearch():
    global combo
    global window

    combo = ttk.Combobox(window,height = 70,width =50,state='readonly')
    combo['values'] = ('시간별 국제선','시간별 국내선','공항별 국내선','종합 날씨 조회','면세점 시설 검색','비면세점 시설 검색','인천공항 지도 사이트 연결','이메일 전송','c++연동')

    combo.place(x=255,y=100)
    action = ttk.Button(window,text ='검색',command=SearchButtonAction)
    action.place(x=642,y=99)

def SearchButtonAction():
    global menu
    global combo

    s=combo.get()
    destroy()
    if s==menu['0']:
        #시간별 국내선
        Inter_airline()
    elif s == menu['1']:
        #시간별 국제선
        dom_airline()
    elif s ==menu['2']:
        #공항별 국제선
        airportDomainSearch()
    elif s == menu['3']:
        #종합 날씨 조회
        Wheather()
    elif s == menu['4']:
        #면세점 조회
        searchDutyFacilities()
    elif s == menu['5']:
        #비면세점 조회
        SearchNoDutyFacilities()
    elif s == menu['6']:
        Map()
    elif s == menu['7'] :
        emailsend()
    elif s== menu['8']:
        cpp()

def Inter_airline():
    global window
    global entry1,entry2
    global Label1,Label2
    global button1

    RenderText.delete(0.0, END)

    TempFont = font.Font(window,size=15,weight ='bold',family='Consolas')
    Label1 = Label(window, relief='solid', pady=4, padx=5, bg='white', bd=1.4, text='예정시간을 입력하세요(00:00~24:00)')
    Label2 = Label(window, relief='solid', pady=4, padx=5, bg='white', bd=1.4, text='변경시간을 입력하세요(00:00~24:00)')
    Label1.place(x=240, y=151)
    Label2.place(x=240, y=205)
    entry1 = Entry(window, font=TempFont, width=17, relief='raised', bd=2.4)
    entry2 = Entry(window, font=TempFont, width=17, relief='raised', bd=2.4)
    entry1.place(x=480, y=149)
    entry2.place(x=480, y=203)
    button1 = Button(window, text='입력', command=InterStimeToGet)
    button1.place(x=700, y=174)

def InterStimeToGet():
    global entry1
    global entry2
    global key

    startTime = entry1.get()
    endTime = entry2.get()

    RenderText.delete(0.0, END)

    url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey=' + key + '&schStTime=' + startTime + '&schEdTime=' + endTime + '&schLineType=I'
    resp = None
    try:
        resp = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print(e.reason)
        print(urllib.request.parseString(e.read().decode('utf-8')).toprettyxml())
    except urllib.error.HTTPError as e:
        print("error code=" + e.code)
        print(urllib.request.parseString(e.read().decode('utf-8')).toprettyxml())
    else:
        response_body = resp.read()

        root = etree.fromstring(response_body)


        RenderText.insert(INSERT,' ============입력하신 시간대 운항 정보입니다.============\n')

        for child in root.iter('item'):

            airfin = child.find('airFln').text            #항공편명
            if child.find('airlineEnglish') != None:
                airline_english = child.find('airlineEnglish').text          #항공사(영문)
            if child.find('airlineKorean') != None:
                airline_korean = child.find('airlineKorean').text   #항공사 (국문)
            airport = child.find('airport').text                 #기준 공항 코드
            arrival_airport = child.find('arrivedKor').text                    #도착 공항(국문)
            boarding_airport = child.find('boardingKor').text                 #출발공항(국문)
            city = child.find('city').text      #운항구간 코드
            inout = child.find('io').text    #출/도착 코드
            line = child.find('line').text   #국내 국제 코드
            std = child.find('std').text     #예정시간

            if airline_korean != None and airline_english !=None:
                RenderText.insert(INSERT,'\n 항공편명 = ')
                RenderText.insert(INSERT,airfin)
                RenderText.insert(INSERT, '\n 항공사(영어) = ')
                RenderText.insert(INSERT, airline_english)
                RenderText.insert(INSERT, '\n 항공사(한글) = ')
                RenderText.insert(INSERT, airline_korean)
                RenderText.insert(INSERT, '\n 기준공항 코드 = ')
                RenderText.insert(INSERT, airport)
                RenderText.insert(INSERT, '\n 출발 공항 = ')
                RenderText.insert(INSERT, boarding_airport)
                RenderText.insert(INSERT, '\n 도착 공항 = ')
                RenderText.insert(INSERT, arrival_airport)
                RenderText.insert(INSERT, '\n 운항 구간 코드 = ')
                RenderText.insert(INSERT, city)
                RenderText.insert(INSERT, '\n 출/도착 = ')
                RenderText.insert(INSERT, inout)
                RenderText.insert(INSERT, '\n 국내 국제 코드 = ')
                RenderText.insert(INSERT, line)
                RenderText.insert(INSERT, '\n 예정 시간 = ')
                RenderText.insert(INSERT, std)
                RenderText.insert(INSERT, '\n\n\n')
            elif airline_korean==None:
                RenderText.insert(INSERT, '\n 항공편명 = ')
                RenderText.insert(INSERT, airfin)
                RenderText.insert(INSERT, '\n 항공사(영어) = ')
                RenderText.insert(INSERT, airline_english)
                RenderText.insert(INSERT, '\n 기준공항 코드 = ')
                RenderText.insert(INSERT, airport)
                RenderText.insert(INSERT, '\n 출발 공항 = ')
                RenderText.insert(INSERT, boarding_airport)
                RenderText.insert(INSERT, '\n 도착 공항 = ')
                RenderText.insert(INSERT, arrival_airport)
                RenderText.insert(INSERT, '\n 운항 구간 코드 = ')
                RenderText.insert(INSERT, city)
                RenderText.insert(INSERT, '\n 출/도착 = ')
                RenderText.insert(INSERT, inout)
                RenderText.insert(INSERT, '\n 국내 국제 코드 = ')
                RenderText.insert(INSERT, line)
                RenderText.insert(INSERT, '\n 예정 시간 = ')
                RenderText.insert(INSERT, std)
                RenderText.insert(INSERT, '\n\n\n')
            elif airline_english ==None:
                RenderText.insert(INSERT, '\n 항공편명 = ')
                RenderText.insert(INSERT, airfin)
                RenderText.insert(INSERT, '\n 항공사(한글) = ')
                RenderText.insert(INSERT, airline_korean)
                RenderText.insert(INSERT, '\n 기준공항 코드 = ')
                RenderText.insert(INSERT, airport)
                RenderText.insert(INSERT, '\n 출발 공항 = ')
                RenderText.insert(INSERT, boarding_airport)
                RenderText.insert(INSERT, '\n 도착 공항 = ')
                RenderText.insert(INSERT, arrival_airport)
                RenderText.insert(INSERT, '\n 운항 구간 코드 = ')
                RenderText.insert(INSERT, city)
                RenderText.insert(INSERT, '\n 출/도착 = ')
                RenderText.insert(INSERT, inout)
                RenderText.insert(INSERT, '\n 국내 국제 코드 = ')
                RenderText.insert(INSERT, line)
                RenderText.insert(INSERT, '\n 예정 시간 = ')
                RenderText.insert(INSERT, std)
                RenderText.insert(INSERT, '\n\n\n')

def dom_airline():
    global window
    global entry1,entry2
    global Label1,Label2
    global button1

    RenderText.delete(0.0, END)

    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    Label1 = Label(window,relief='solid',pady=4,padx=5,bg='white',bd=1.4, text='예정시간을 입력하세요(00:00~24:00)')
    Label2 = Label(window,relief='solid',pady=4,padx=5,bg='white',bd=1.4, text='변경시간을 입력하세요(00:00~24:00)')
    Label1.place(x=240, y=151)
    Label2.place(x=240, y=205)
    entry1 = Entry(window, font = TempFont, width = 17,relief = 'raised',bd=2.4)
    entry2 = Entry(window, font = TempFont, width = 17,relief = 'raised',bd=2.4)
    entry1.place(x=480, y=149)
    entry2.place(x=480, y=203)
    button1 = Button(window, text='입력', command=DomStimeToGet)
    button1.place(x=700, y=174)


def DomStimeToGet():
    global startTime
    global endTime
    global entry1,entry2
    global key

    startTime = entry1.get()
    endTime = entry2.get()

    url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey=' + key + '&schStTime=' + startTime + '&schEdTime=' + endTime + '&schLineType=D'
    resp = None
    try:
        resp = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print(e.reason)
        print(urllib.request.parseString(e.read().decode('utf-8')).toprettyxml())
    except urllib.error.HTTPError as e:
        print("error code=" + e.code)
        print(urllib.request.parseString(e.read().decode('utf-8')).toprettyxml())
    else:
        response_body = resp.read()

        root = etree.fromstring(response_body)

        RenderText.delete(0.0, END)
        RenderText.insert(INSERT, ' 입력하신 시간대의 운항 정보입니다.============\n')

        for child in root.iter('item'):
            airfin = child.find('airFln').text  # 항공편명
            airline_english = child.find('airlineEnglish').text  # 항공사(영문)
            airline_korean = child.find('airlineKorean').text  # 항공사 (국문)
            airport = child.find('airport').text  # 기준 공항 코드
            arrival_airport = child.find('arrivedKor').text  # 도착 공항(국문)
            boarding_airport = child.find('boardingKor').text  # 출발공항(국문)
            city = child.find('city').text  # 운항구간 코드
            # estimate_time = child.find('etd') # 변경시간
            # gatenumber = child.find('gate').text #게이트 번호
            inout = child.find('io').text  # 출/도착 코드
            line = child.find('line').text  # 국내 국제 코드
            # airstatus = child.find('rmkKor').text #항공편 상태
            std = child.find('std').text  # 예정시간

            # print('항공편명 = '+airfin+'\n항공사(영어) = '+airline_english+'\n항공사(한글) = '+airline_korean+'\n기준공항 코드 = '+airport+'\n도착 공항 = '+arrival_airport+'\n출발 공항 = '+boarding_airport+
            #     '\n운항구간 코드= '+city+'\n출/도착코드 = '+inout+'\n국내 국제 코드 = '+line+'\n예정 시간 = '+std)
            RenderText.insert(INSERT, '\n 항공편명 = ')
            RenderText.insert(INSERT, airfin)
            RenderText.insert(INSERT, '\n 항공사(영어) = ')
            RenderText.insert(INSERT, airline_english)
            RenderText.insert(INSERT, '\n 항공사(한글) = ')
            RenderText.insert(INSERT, airline_korean)
            RenderText.insert(INSERT, '\n 기준공항 코드 = ')
            RenderText.insert(INSERT, airport)
            RenderText.insert(INSERT, '\n 출발 공항 = ')
            RenderText.insert(INSERT, boarding_airport)
            RenderText.insert(INSERT, '\n 도착 공항 = ')
            RenderText.insert(INSERT, arrival_airport)
            RenderText.insert(INSERT, '\n 운항 구간 코드 = ')
            RenderText.insert(INSERT, city)
            RenderText.insert(INSERT, '\n 출/도착 = ')
            RenderText.insert(INSERT, inout)
            RenderText.insert(INSERT, '\n 국내 국제 코드 = ')
            RenderText.insert(INSERT, line)
            RenderText.insert(INSERT, '\n 예정 시간 = ')
            RenderText.insert(INSERT, std)
            RenderText.insert(INSERT, '\n\n\n')

def airportGet():
    global entry1,entry2

    airport = entry1.get()
    time = entry2.get()
    url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey=' + key + \
          "&schStTime=" + time + '&schEdTime=2400&schLineType=D&schAirCode=' + airport

    RenderText.delete(0.0, END)

    RenderText.insert(INSERT, "=============공항코드 정보=================\n")
    RenderText.insert(INSERT, "김포 = GMP  김해 = PUS  대구 = TAE  제주 = CJU  \n광주 = KWJ  청주 = CJJ  포항 = KPO  ")
    RenderText.insert(INSERT, "울산 = USN  \n진주 = HIN  원주 = WJU  양양 = YNY  여수 = RSU  \n목포 = MPK  군산 = KUV  무안 = MWX")
    RenderText.insert(INSERT, "\n=========================================\n")

    data = urllib.request.urlopen(url).read()

    root = etree.fromstring(data)
    for child in root.iter("item"):
        airline = child.find('airlineKorean').text
        start = child.find('boardingKor').text
        end = child.find('arrivedKor').text
        startTime = child.find('std').text

        RenderText.insert(INSERT,'\n 항공사 = ')
        RenderText.insert(INSERT, airline)
        RenderText.insert(INSERT,'\n 출발 공항 = ')
        RenderText.insert(INSERT, start)
        RenderText.insert(INSERT,'\n 도착 공항 = ')
        RenderText.insert(INSERT,end)
        RenderText.insert(INSERT,'\n 출발 시간 = ')
        RenderText.insert(INSERT,startTime)
        RenderText.insert(INSERT, '\n\n\n')


def airportDomainSearch():
    global entry1,entry2
    global Label1,Label2
    global button1

    RenderText.delete(0.0, END)

    RenderText.insert(INSERT,"=============공항코드 정보=================\n")
    RenderText.insert(INSERT,"김포 = GMP  김해 = PUS  대구 = TAE  제주 = CJU  \n광주 = KWJ  청주 = CJJ  포항 = KPO  ")
    RenderText.insert(INSERT,"울산 = USN  \n진주 = HIN  원주 = WJU  양양 = YNY  여수 = RSU  \n목포 = MPK  군산 = KUV  무안 = MWX")
    RenderText.insert(INSERT,"\n=========================================\n")

    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    Label1 = Label(window,relief='solid', pady=4, padx=5, bg='white', bd=1.4,text="공항 코드를 입력하세요 ")
    Label2 = Label(window,relief='solid', pady=4, padx=5, bg='white', bd=1.4,text="시간대를 입력하세요 (00:00~24:00) ")
    Label1.place(x=267, y=151)
    Label2.place(x=230, y=205)
    entry1 = Entry(window, font=TempFont, width=17, relief='raised', bd=2.4)
    entry2 = Entry(window, font=TempFont, width=17, relief='raised', bd=2.4)
    entry1.place(x=450, y=149)
    entry2.place(x=450, y=203)
    button1 = Button(window, text='입력', command=airportGet)
    button1.place(x=670, y=174)

def Wheather():
    global wheathercombo
    global window

    RenderText.delete(0.0, END)

    url = "http://newsky2.kma.go.kr/service/VilageFrcstDspthDocInfoService/WidGeneralWeatherCondition?ServiceKey=QydOrzDVYNDcxRwTCTjElQ8FWVC7fQgJ8JVlglIlMmFtva3gU65%2BRmV%2FlyxorjQzmRAiXGxM%2F2E1PXAC56NWdg%3D%3D&stnId=108"

    resp = None
    try:
        resp = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print(e.reason)
        print(urllib.request.parseString(e.read().decode('utf-8')).toprettyxml())
    except urllib.error.HTTPError as e:
        print("error code=" + e.code)
        print(urllib.request.parseString(e.read().decode('utf-8')).toprettyxml())
    else:
        response_body = resp.read()

        root = etree.fromstring(response_body)

        RenderText.delete(0.0, END)

        for child in root.iter('item'):
            btime = child.find('tmFc').text  # 발표시간
            today = child.find('wfSv1').text  # 오늘 날씨

            RenderText.insert(INSERT, '\n 발표시간 = ')
            RenderText.insert(INSERT, btime)
            RenderText.insert(INSERT, '\n 종합날씨 = ')
            RenderText.insert(INSERT, today)

def searchDutyFacilities():
    global combo1
    global button1

    combo1 = ttk.Combobox(window, height=70, width=50, state='readonly')
    combo1['values'] = ('신라면세점', '롯데면세점', 'SM면세점', '신세계면세점','엔타스면세점','시티면세점','삼익면세점')

    combo1.place(x=255, y=160)
    button1 = ttk.Button(window, text='검색', command=DutyGet)
    button1.place(x=642, y=157)

def DutyGet():
    global Label1
    global entry1
    global duty
    global button2
    global combo1

    from urllib import parse

    RenderText.delete(0.0, END)

    facility = combo1.get()
    duty = facility
    encode = parse.quote(facility)

    url = 'http://openapi.airport.kr/openapi/service/FacilitiesInformation/getFacilitesInfo?serviceKey=' + key + '&pageNo=1&startPage=1&numOfRows=176&pageSize=10&lang=K&lcduty=Y&facilitynm=' + encode

    resp = None
    try:
        resp = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print(e.reason)
        print(urllib.request.parseString(e.read().decode('utf-8')).toprettyxml())
    except urllib.error.HTTPError as e:
        print("error code=" + e.code)
        print(urllib.request.parseString(e.read().decode('utf-8')).toprettyxml())
    else:
        response_body = resp.read()
        root = etree.fromstring(response_body)

        TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
        Label1 = Label(window, relief='solid', pady=4, padx=5, bg='white', bd=1.4, text="키워드를 입력하세요")
        Label1.place(x=290,y=220)
        entry1 = Entry(window, font = TempFont, width = 13,relief = 'raised',bd=2.4)
        entry1.place(x=440, y=219)
        RenderText.insert(INSERT,
                          '\n검색 키워드:    주류      담배     식품      화장품  \n\t\t국산      기념품   유아      완구  \n\t\t전자제품  패션     악세사리  향수  \n\t\t가방      신발     시계      럭셔리  \n\t\t한국      지갑     복합매장')
        button2 = Button(window, text='입력', command=SearchSubfacilities)
        button2.place(x=600, y=220)

def SearchSubfacilities():
    global RenderText
    global dic
    global duty
    from urllib import parse

    facility = duty
    RenderText.delete(0.0, END)

    encode = parse.quote(facility)

    url = 'http://openapi.airport.kr/openapi/service/FacilitiesInformation/getFacilitesInfo?serviceKey=' + key + '&pageNo=1&startPage=1&numOfRows=176&pageSize=10&lang=K&lcduty=Y&facilitynm=' + encode

    resp = None
    try:
        resp = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print(e.reason)
        print(urllib.request.parseString(e.read().decode('utf-8')).toprettyxml())
    except urllib.error.HTTPError as e:
        print("error code=" + e.code)
        print(urllib.request.parseString(e.read().decode('utf-8')).toprettyxml())
    else:
        response_body = resp.read()
        root = etree.fromstring(response_body)

    count = 0
    for child in root.iter('item'):
        sn = child.find('sn').text  # 시설별 시퀀스 번호
        facilityItem = child.find('facilityitem').text  # 취급품목
        facilityName = child.find('facilitynm').text  # 시설명 or 매장명
        location = child.find('lcnm').text  # 시설 위치 설명
        if child.find('goods') != None:
            goods = child.find('goods').text  # 취급품목 브랜드
        else:
            goods = None
        servicetime = child.find('servicetime').text  # 서비스 시간
        if child.find('terminalid') != None:
            terminalid = child.find('terminalid').text  # 터미널 구분
        else:
            terminalid = None
        floor = child.find('floorinfo').text  # 층 구분
        if child.find('tel') != None:
            tel = child.find('tel').text  # 전화번호
        else:
            tel = None

        if entry1.get() in facilityName:
            count += 1
            if tel == None and terminalid == None and goods != None:
                RenderText.insert(INSERT, '\n시설별 시퀀스 번소 = ')
                RenderText.insert(INSERT, sn)
                RenderText.insert(INSERT, '\n취급 품목 = ')
                RenderText.insert(INSERT, facilityItem)
                RenderText.insert(INSERT, '\n시설명/매장명 = ')
                RenderText.insert(INSERT, facilityName)
                RenderText.insert(INSERT, '\n시설 위치 = ')
                RenderText.insert(INSERT, location)
                RenderText.insert(INSERT, '\n취급 품목 브랜드 =')
                RenderText.insert(INSERT, goods)
                RenderText.insert(INSERT, '\n서비스 시간 = ')
                RenderText.insert(INSERT, servicetime)
                RenderText.insert(INSERT, '\n층 = ')
                RenderText.insert(INSERT, floor)
                RenderText.insert(INSERT, "\n\n\n")
            elif tel == None and terminalid != None:
                # print(
                #    '\n시설별 시퀀스 번호=' + sn + '\n취급 품목 =' + facilityItem + '\n시설명/매장명 =' + facilityName + '\n시설 위치 =' + location + '\n서비스 시간 =' + servicetime + \
                #    '\n터미널 =' + terminalid + '\n층 =' + floor)
                RenderText.insert(INSERT, '\n시설별 시퀀스 번소 = ')
                RenderText.insert(INSERT, sn)
                RenderText.insert(INSERT, '\n취급 품목 = ')
                RenderText.insert(INSERT, facilityItem)
                RenderText.insert(INSERT, '\n시설명/매장명 = ')
                RenderText.insert(INSERT, facilityName)
                RenderText.insert(INSERT, '\n시설 위치 = ')
                RenderText.insert(INSERT, location)
                RenderText.insert(INSERT, '\n서비스 시간 = ')
                RenderText.insert(INSERT, servicetime)
                RenderText.insert(INSERT, '\n층 = ')
                RenderText.insert(INSERT, floor)
                RenderText.insert(INSERT, '\n터미널 = ')
                RenderText.insert(INSERT, terminalid)
                RenderText.insert(INSERT, "\n\n\n")
            elif goods == None:
                # print(
                #    '\n시설별 시퀀스 번호=' + sn + '\n취급 품목 =' + facilityItem + '\n시설명/매장명 =' + facilityName + '\n시설 위치 =' + location + '\n서비스 시간 =' + servicetime + \
                #   '\n터미널 =' + terminalid + '\n층 =' + floor + '\n전화번호 =' + tel)
                RenderText.insert(INSERT, '\n시설별 시퀀스 번소 = ')
                RenderText.insert(INSERT, sn)
                RenderText.insert(INSERT, '\n취급 품목 = ')
                RenderText.insert(INSERT, facilityItem)
                RenderText.insert(INSERT, '\n시설명/매장명 = ')
                RenderText.insert(INSERT, facilityName)
                RenderText.insert(INSERT, '\n시설 위치 = ')
                RenderText.insert(INSERT, location)
                RenderText.insert(INSERT, '\n서비스 시간 = ')
                RenderText.insert(INSERT, servicetime)
                RenderText.insert(INSERT, '\n층 = ')
                RenderText.insert(INSERT, floor)
                RenderText.insert(INSERT, '\n터미널 = ')
                RenderText.insert(INSERT, terminalid)
                RenderText.insert(INSERT, '\n전화번호 = ')
                RenderText.insert(INSERT, tel)
                RenderText.insert(INSERT, "\n\n\n")

            elif terminalid == None:
                # print(
                #    '\n시설별 시퀀스 번호=' + sn + '\n취급 품목 =' + facilityItem + '\n시설명/매장명 =' + facilityName + '\n시설 위치 =' + location + '\n취급 품목 브랜드 =' + goods + '\n서비스 시간 =' + servicetime + \
                #    '\n층 =' + floor + '\n전화번호 =' + tel)
                RenderText.insert(INSERT, '\n시설별 시퀀스 번소 = ')
                RenderText.insert(INSERT, sn)
                RenderText.insert(INSERT, '\n취급 품목 = ')
                RenderText.insert(INSERT, facilityItem)
                RenderText.insert(INSERT, '\n시설명/매장명 = ')
                RenderText.insert(INSERT, facilityName)
                RenderText.insert(INSERT, '\n시설 위치 = ')
                RenderText.insert(INSERT, location)
                RenderText.insert(INSERT, '\n취급 품목 브랜드 = ')
                RenderText.insert(INSERT, goods)
                RenderText.insert(INSERT, '\n서비스 시간 = ')
                RenderText.insert(INSERT, servicetime)
                RenderText.insert(INSERT, '\n층 = ')
                RenderText.insert(INSERT, floor)
                RenderText.insert(INSERT, '\n전화번호 = ')
                RenderText.insert(INSERT, tel)
                RenderText.insert(INSERT, "\n\n\n")
            elif tel != None and goods != None:
                # print(
                #    '\n시설별 시퀀스 번호=' + sn + '\n취급 품목 =' + facilityItem + '\n시설명/매장명 =' + facilityName + '\n시설 위치 =' + location + '\n취급 품목 브랜드 =' + goods + '\n서비스 시간 =' + servicetime + \
                #    '\n터미널 =' + terminalid + '\n층 =' + floor + '\n전화번호 =' + tel)
                RenderText.insert(INSERT, '\n시설별 시퀀스 번소 = ')
                RenderText.insert(INSERT, sn)
                RenderText.insert(INSERT, '\n취급 품목 = ')
                RenderText.insert(INSERT, facilityItem)
                RenderText.insert(INSERT, '\n시설명/매장명 = ')
                RenderText.insert(INSERT, facilityName)
                RenderText.insert(INSERT, '\n시설 위치 = ')
                RenderText.insert(INSERT, location)
                RenderText.insert(INSERT, '\n취급 품목 브랜드 = ')
                RenderText.insert(INSERT, goods)
                RenderText.insert(INSERT, '\n서비스 시간 = ')
                RenderText.insert(INSERT, servicetime)
                RenderText.insert(INSERT, '\n층 = ')
                RenderText.insert(INSERT, floor)
                RenderText.insert(INSERT, '\n전화번호 = ')
                RenderText.insert(INSERT, tel)
                RenderText.insert(INSERT, '\n터미널 = ')
                RenderText.insert(INSERT, terminalid)
                RenderText.insert(INSERT, "\n\n\n")

    if count == 0:
        RenderText.insert(INSERT, '\n해당 품목이 면세점에 없습니다.')


def SearchNoDutyFacilities():
    global combo1
    global Label1,Label2
    global entry1,entry2
    global button1,button2
    global window

    RenderText.delete(0.0, END)

    combo1 = ttk.Combobox(window, height=70, width=50, state='readonly')
    combo1['values'] = ('공항시설', '공항명소', '일반쇼핑', '음식점')

    combo1.place(x=255, y=160)
    button1 = ttk.Button(window, text='검색', command=NoDutyAction)
    button1.place(x=642, y=157)

def NoDutyAction():
    from urllib import parse
    global combo1
    global window
    global entry1
    global Label1
    global button2

    #key = 'QydOrzDVYNDcxRwTCTjElQ8FWVC7fQgJ8JVlglIlMmFtva3gU65%2BRmV%2FlyxorjQzmRAiXGxM%2F2E1PXAC56NWdg%3D%3D'
    url = 'http://openapi.airport.kr/openapi/service/FacilitiesInformation/getFacilitesInfo?serviceKey=' + key + '&pageNo=1&startPage=1&numOfRows=320&pageSize=320&lang=K&lcduty=N'

    resp = None
    try:
        resp = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print(e.reason)
        print(urllib.request.parseString(e.read().decode('utf-8')).toprettyxml())
    except urllib.error.HTTPError as e:
        print("error code=" + e.code)
        print(urllib.request.parseString(e.read().decode('utf-8')).toprettyxml())
    else:
        response_body = resp.read()

        root = etree.fromstring(response_body)
    store = combo1.get()
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    RenderText.delete(0.0, END)

    for child in root.iter('item'):
        if store in child.find('lcategorynm').text:
            RenderText.insert(INSERT,child.find('facilitynm').text)
            RenderText.insert    (INSERT, '\n')
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    Label1 = Label(window, relief='solid', pady=4, padx=5, bg='white', bd=1.4, text='상세하게 알고싶은 가게명을 입력하세요')
    Label1.place(x=205, y=215)
    entry1 = Entry(window, font = TempFont, width = 22,relief = 'raised',bd=2.4)
    entry1.place(x=451, y=215)
    button2 = Button(window, text='입력', command=NoDutyName)
    button2.place(x=720, y=215)

def NoDutyName():

    global NoDutyEntry

    url = 'http://openapi.airport.kr/openapi/service/FacilitiesInformation/getFacilitesInfo?serviceKey=' + key + '&pageNo=1&startPage=1&numOfRows=320&pageSize=320&lang=K&lcduty=N'

    resp = None
    try:
        resp = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print(e.reason)
        print(urllib.request.parseString(e.read().decode('utf-8')).toprettyxml())
    except urllib.error.HTTPError as e:
        print("error code=" + e.code)
        print(urllib.request.parseString(e.read().decode('utf-8')).toprettyxml())
    else:
        response_body = resp.read()

        root = etree.fromstring(response_body)

    store = entry1.get()
    RenderText.delete(0.0, END)

    for child in root.iter('item'):
        if store in child.find('facilitynm').text:
            name = child.find('facilitynm').text
            floor = child.find('floorinfo').text
            location = child.find('lcnm').text
            servicetime = child.find('servicetime').text
            serialnum = child.find('sn').text
            if child.find('tel') != None:
                tel = child.find('tel').text
            else:
                tel = None
            terminalId = child.find('terminalid').text

            if tel != None:
                RenderText.insert(INSERT, '\n가게 이름 : ')
                RenderText.insert(INSERT, name)
                RenderText.insert(INSERT, '\n층 : ')
                RenderText.insert(INSERT, floor)
                RenderText.insert(INSERT, '\n매장위치 : ')
                RenderText.insert(INSERT, location)
                RenderText.insert(INSERT, '\n영업시간 : ')
                RenderText.insert(INSERT, servicetime)
                RenderText.insert(INSERT, '\n매장번호 : ')
                RenderText.insert(INSERT, serialnum)
                RenderText.insert(INSERT, '\n전화번호 : ')
                RenderText.insert(INSERT, tel)
                RenderText.insert(INSERT, '\n터미널 : ')
                RenderText.insert(INSERT, terminalId)
                RenderText.insert(INSERT, '\n\n\n')

            elif tel == None:
                RenderText.insert(INSERT, '\n가게 이름 : ')
                RenderText.insert(INSERT, name)
                RenderText.insert(INSERT, '\n층 : ')
                RenderText.insert(INSERT, floor)
                RenderText.insert(INSERT, '\n매장위치 : ')
                RenderText.insert(INSERT, location)
                RenderText.insert(INSERT, '\n영업시간 : ')
                RenderText.insert(INSERT, servicetime)
                RenderText.insert(INSERT, '\n매장번호 : ')
                RenderText.insert(INSERT, serialnum)
                RenderText.insert(INSERT, '\n터미널 : ')
                RenderText.insert(INSERT, terminalId)
                RenderText.insert(INSERT,'\n\n\n')

def Map():
    global entry1
    global Label1
    global button1

    RenderText.delete(0.0, END)

    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    RenderText.insert(INSERT,"==========인천공항 지도를 웹으로 연결하시겠습니까?===========\n\n\n")
    RenderText.insert(INSERT,"\n======================예/아니오==========================\n")
    Label1 = Label(window,font=TempFont,relief='solid',bg='white',fg='black', pady=4, padx=5, bd=1.4,text='예/아니오')
    Label1.place(x=430,y=145)
    entry1 = Entry(window, font = TempFont, width = 10,relief = 'raised',bd=2.4)
    entry1.place(x=421,y=186)
    button1 = Button(window,font = TempFont, text='입력', command=mapAction)
    button1.place(x=450, y=220)

def mapAction():
    global entry1

    if entry1.get() == '예':
        RenderText.insert(INSERT,'\n인천공항 지도 보기를 선택하였습니다.')
        new_url = 'https://www.airport.kr/ap/ko/map/mapInfo.do'
        return webbrowser.open_new(new_url)
    else:
        RenderText.insert(INSERT,'\n공항 지도 연결을 건너뛰었습니다.')

def destroy():

    if 'entry1' in globals():
        entry1.destroy()
    if 'entry2' in globals():
        entry2.destroy()
    if 'Label1' in globals():
        Label1.destroy()
    if 'Label2' in globals():
        Label2.destroy()
    if 'button1' in globals():
        button1.destroy()
    if 'button2' in globals():
        button2.destroy()
    if 'combo1' in globals():
        combo1.destroy()
def emailsend():
    global window
    global Label3
    global entry1
    global button1


    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    Label3 = Label(window, relief='solid', pady=4, padx=5, bg='white', bd=1.4, text='이메일 주소')
    Label3.place(x=305, y=155)
    entry1 = Entry(window, font=TempFont, width=22, relief='raised', bd=2.4)
    entry1.place(x=401, y=155)
    button1 = Button(window, text='이메일 전송', command=emailaction)
    button1.place(x=430, y=210)

def emailaction():
    import spam
    global window
    global Label1
    global entry1
    global button1


    text = RenderText.get("1.0",END)

    gmail_user = "ekdskrnl105@gmail.com"
    gmail_pw = 'tkaudwls12!'

    to_addr = entry1.get()

    msg = MIMEMultipart('alternative')
    msg['From'] = gmail_user
    msg['To'] = to_addr
    msg['Subject'] = '항공정보'  # 제목
    msg.attach(MIMEText(text, 'plain', 'utf-8'))  # 내용 인코딩

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pw)
        server.sendmail(gmail_user, to_addr, msg.as_string())
        server.quit()
        print('success sent mail')

    except BaseException as e:
        print("failed send mail", str(e))


def cpp():
    global window
    global Label1
    global entry1
    global button1

    RenderText.delete(0.0, END)
    TempFont = font.Font(window, size=15, weight='bold', family='Consolas')
    Label1 = Label(window, relief='solid', pady=4, padx=5, bg='white', bd=1.4, text='c++ 연동')
    Label1.place(x=305, y=155)
    entry1 = Entry(window, font=TempFont, width=22, relief='raised', bd=2.4)
    entry1.place(x=401, y=155)
    button1 = Button(window, text='c++연동하기', command=cppaction)
    button1.place(x=430, y=210)

def cppaction():
    import spam
    global entry1
    global RenderText

    RenderText.delete(0.0, END)

    s=str(entry1.get())
    s=spam.strlen(s)

    RenderText.insert(INSERT,'문자열 개수 길이\n')
    RenderText.insert(INSERT,s)




window.geometry("950x700+350+70")
photo = PhotoImage(file="airplane.gif")
imageLabel = Label(window, image=photo)
imageLabel.pack()


TopText()
InitRenderText()
MainSearch()
bot = noti.telepot.Bot(noti.TOKEN)
bot.message_loop(noti.handle)

window.mainloop()
