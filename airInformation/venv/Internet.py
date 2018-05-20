from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request
import xml.etree.ElementTree as etree
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import webbrowser


class Airport:
    def __init__(self,name):
        self.name = name
        self.latitudeX = 0.0
        self.latitudeY = 0.0

    def __str__(self):
        return self.name



#국제 항공편 검색
def inter_airline():
    print("=========공항코드 정보==========")

    stime = input("예정시간을 입력하세요:")
    etime = input("변경시간을 입력하세요:")
    key = 'QydOrzDVYNDcxRwTCTjElQ8FWVC7fQgJ8JVlglIlMmFtva3gU65%2BRmV%2FlyxorjQzmRAiXGxM%2F2E1PXAC56NWdg%3D%3D'
    url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey='+key+'&schStTime='+stime+'&schEdTime='+etime+'&schLineType=I'
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

        answer= '입력하신 공항의 운항 정보입니다.\n=================================='
        print(answer)

        for child in root.iter('item'):
            airfin = child.find('airFln').text            #항공편명
            airline_english = child.find('airlineEnglish').text          #항공사(영문)
            airline_korean = child.find('airlineKorean').text   #항공사 (국문)
            airport = child.find('airport').text                 #기준 공항 코드
            arrival_airport = child.find('arrivedKor').text                    #도착 공항(국문)
            boarding_airport = child.find('boardingKor').text                 #출발공항(국문)
            city = child.find('city').text      #운항구간 코드
            estimate_time = child.find('etd') # 변경시간
            #gatenumber = child.find('gate').text #게이트 번호
            inout = child.find('io').text    #출/도착 코드
            line = child.find('line').text   #국내 국제 코드
            #airstatus = child.find('rmkKor').text #항공편 상태
            std = child.find('std').text     #예정시간


            print('항공편명 = '+airfin+'\n항공사(영어) = '+airline_english+'\n항공사(한글) = '+airline_korean+'\n기준공항 코드 = '+airport+'\n도착 공항 = '+arrival_airport+'\n출발 공항 = '+boarding_airport+
                  '\n운항구간 코드= '+city+'\n출/도착코드 = '+inout+'\n국내 국제 코드 = '+line+'\n예정 시간 = '+std)




            print("==============================\n\n=========================================")

#국재 항공편 검색
def dom_airline():
    print("=========공항코드 정보==========")

    stime = input("예정시간을 입력하세요:")
    etime = input("변경시간을 입력하세요:")
    key = 'QydOrzDVYNDcxRwTCTjElQ8FWVC7fQgJ8JVlglIlMmFtva3gU65%2BRmV%2FlyxorjQzmRAiXGxM%2F2E1PXAC56NWdg%3D%3D'
    url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey='+key+'&schStTime='+stime+'&schEdTime='+etime+'&schLineType=D'
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

        answer= '입력하신 공항의 운항 정보입니다.\n=================================='
        print(answer)

        for child in root.iter('item'):
            airfin = child.find('airFln').text            #항공편명
            airline_english = child.find('airlineEnglish').text          #항공사(영문)
            airline_korean = child.find('airlineKorean').text   #항공사 (국문)
            airport = child.find('airport').text                 #기준 공항 코드
            arrival_airport = child.find('arrivedKor').text                    #도착 공항(국문)
            boarding_airport = child.find('boardingKor').text                 #출발공항(국문)
            city = child.find('city').text      #운항구간 코드
            estimate_time = child.find('etd') # 변경시간
            #gatenumber = child.find('gate').text #게이트 번호
            inout = child.find('io').text    #출/도착 코드
            line = child.find('line').text   #국내 국제 코드
            #airstatus = child.find('rmkKor').text #항공편 상태
            std = child.find('std').text     #예정시간


            print('항공편명 = '+airfin+'\n항공사(영어) = '+airline_english+'\n항공사(한글) = '+airline_korean+'\n기준공항 코드 = '+airport+'\n도착 공항 = '+arrival_airport+'\n출발 공항 = '+boarding_airport+
                  '\n운항구간 코드= '+city+'\n출/도착코드 = '+inout+'\n국내 국제 코드 = '+line+'\n예정 시간 = '+std)




            print("==============================\n\n=========================================")


def weather():
    print("==============공항 코드===============")
    print("RKSI 인천공항 RKSS 김포공항 RKPC 제주공항\n RKPK 김해공항 RKNY 양양공항 RKNW 원주공항 \nRKTU 청주공항 RKTN 대구공항 RKTH 포항공항\n"
          " RKJJ 광주공항 RKJB 무안공항 RKJY 여수공항 \nRKPU 울산공항 RKPS 사천공항 RKJK 군산공항")

    d = {'RKSI':'인천공항','RKSS':'김포공항','RKPC':'제주공항','RKPK':'김해공항','RKNY':'양양공항','RKNW':'원주공항','RKTU':'청주공항','RKTN':'대구공항','RKTH':'포항공항',"RKJJ":'광주공항',\
         "RKJB":'무안공항','RKJY':'여수공항','RKPU':'울산공항','RKPS':'사천공항',"RKJK":'군산공항'}

    print("==============날씨 정보===============")


    key = 'QydOrzDVYNDcxRwTCTjElQ8FWVC7fQgJ8JVlglIlMmFtva3gU65%2BRmV%2FlyxorjQzmRAiXGxM%2F2E1PXAC56NWdg%3D%3D'

    airport = input('원하시는 공항의 코드를 입력하세요')
    if airport not in d.keys():
        print("잘못입력하였습니다.")
        return

    url = "http://amoapi.kma.go.kr/amoApi/metar?icao=" + airport

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

        answer = '입력하신 공항의 날씨 정보입니다.\n=================================='
        print(answer)

        for child in root.iter('item'):
            airport = child.find('airportName').text
            str = child.find('metarMsg').text


            print('공항= '+airport +'일기 정보 = '+str )



