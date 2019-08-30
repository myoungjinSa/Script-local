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


        for child in root.iter("response"):
            s= child.find('totalCount')
            if s == None:
                print("\n       해당 지역은 운행 정보가 없습니다.\n")


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


        for child in root.iter("response"):
            s= child.find('totalCount')
            if s == None:
                print("\n       해당 지역은 운행 정보가 없습니다.\n")
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


def generalWeatherCondition():
    print("========기상 정보==========")


    key = 'QydOrzDVYNDcxRwTCTjElQ8FWVC7fQgJ8JVlglIlMmFtva3gU65%2BRmV%2FlyxorjQzmRAiXGxM%2F2E1PXAC56NWdg%3D%3D'
    url = "http://newsky2.kma.go.kr/service/VilageFrcstDspthDocInfoService/WidGeneralWeatherCondition?ServiceKey="+key+"&stnId=108"

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

    answer = '일주일간의 날씨 정보입니다.\n=================================='
    print(answer)

    for child in root.iter('item'):
        btime=child.find('tmFc').text       #발표시간
        today = child.find('wfSv1').text    #오늘 날씨

        print('\n발표 시간 ='+btime)
        print('\n종합 날씨 ='+today)





def airportDomainSearch():
    print("=============공항코드 정보=================")
    print("김포 = GMP 김해 = PUS  대구 = TAE  제주 = CJU  \n광주 = KWJ  청주 = CJJ  포항 = KPO")
    print("울산 = USN  진주 = HIN 원주 = WJU  양양 = YNY \n여수 = RSU  목포 = MPK  군산 = KUV  무안 = MWX")
    print("==========================================")

    airport = input("공항 코드를 입력하세요 : ")
    time = input("시간대를 입력하세요 : ")

    key = 'QydOrzDVYNDcxRwTCTjElQ8FWVC7fQgJ8JVlglIlMmFtva3gU65%2BRmV%2FlyxorjQzmRAiXGxM%2F2E1PXAC56NWdg%3D%3D'
    url = 'http://openapi.airport.co.kr/service/rest/FlightStatusList/getFlightStatusList?ServiceKey=' + key + \
          "&schStTime=" + time + '&schEdTime=2400&schLineType=D&schAirCode=' + airport

    data = urllib.request.urlopen(url).read()

    root = etree.fromstring(data)
    for child in root.iter("item"):
        airline = child.find('airlineKorean').text
        start = child.find('boardingKor').text
        end = child.find('arrivedKor').text
        startTime = child.find('std').text

        print('항공사 = ' + airline +
              '\n출발시간 = ' + startTime + '\n출발공항 = ' + start + '\n도착공항 = ' + end)
        print('=======================================================')


def searchDutyFacilities():
    from urllib import parse
    print("============면세점 시설 검색================")


    print("\n\n")

    key = 'QydOrzDVYNDcxRwTCTjElQ8FWVC7fQgJ8JVlglIlMmFtva3gU65%2BRmV%2FlyxorjQzmRAiXGxM%2F2E1PXAC56NWdg%3D%3D'

    dic = {'0':'[신라면세점]','1':'[롯데면세점]','2':'[SM면세점]','3':'[신세계면세점]','4':'[엔타스면세점]','5':'[시티면세점]','6':'[삼익면세점]'}
    print('0:신라면세점         1:롯데면세점      2:SM면세점        3:신세계면세점        4:엔타스면세점     5:시티면세점     6:삼익면세점\n')

    facility = input('원하시는 면세점을 입력해주세요:')


    if facility in dic.keys():
        encode = parse.quote(dic[facility])

        # parse.unquote()

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

        print('***시설명으로 입력할 경우:\n ')
        print('검색 키워드: 주류  담배  식품  화장품  \n\t\t국산  기념품   유아   완구  \n\t\t전자제품  패션   악세사리  향수  \n\t\t가방   신발   시계   럭셔리  \n\t\t한국  지갑  복합매장  ')
        print('\n')
        print('***매장명으로 입력할 경우: 찾으시는 매장명을 입력해주세요\n')
        store = input('시설명 또는 매장명을 입력해주세요')

        count =0
        for child in root.iter('item'):
            sn = child.find('sn').text  # 시설별 시퀀스 번호
            facilityItem = child.find('facilityitem').text  #취급품목
            facilityName  = child.find('facilitynm').text   #시설명 or 매장명
            location = child.find('lcnm').text  #시설 위치 설명
            if child.find('goods')!= None:
                goods = child.find('goods').text  # 취급품목 브랜드
            else:
                goods = None
            servicetime = child.find('servicetime').text    #서비스 시간
            if child.find('terminalid')!=None:
                terminalid = child.find('terminalid').text  #터미널 구분
            else:
                terminalid = None
            floor = child.find('floorinfo').text    #층 구분
            if child.find('tel')!= None:
                tel = child.find('tel').text  # 전화번호
            else:
                tel = None

            if store in facilityName:
                count +=1
               # encode2 = parse.quote(facilityName)
                #url = 'http://openapi.airport.kr/openapi/service/FacilitiesInformation/getFacilitesInfo?serviceKey=' + key + '&pageNo=1&startPage=1&numOfRows=176&pageSize=10&lang=K&lcduty=Y&facilitynm=' + encode+' '+encode2
                if tel == None and terminalid == None and goods !=None:
                    print('\n시설별 시퀀스 번호=' + sn + '\n취급 품목 =' + facilityItem + '\n시설명/매장명 =' + facilityName+'\n시설 위치 ='+location+'\n취급 품목 브랜드 ='+goods+'\n서비스 시간 ='+servicetime+\
                        '\n층 ='+floor)
                elif tel ==None and terminalid != None:
                    print('\n시설별 시퀀스 번호=' + sn + '\n취급 품목 =' + facilityItem + '\n시설명/매장명 =' + facilityName + '\n시설 위치 =' + location + '\n서비스 시간 =' + servicetime + \
                        '\n터미널 =' + terminalid + '\n층 =' + floor)
                elif goods == None:
                    print('\n시설별 시퀀스 번호=' + sn + '\n취급 품목 =' + facilityItem + '\n시설명/매장명 =' + facilityName + '\n시설 위치 =' + location + '\n서비스 시간 =' + servicetime + \
                        '\n터미널 =' + terminalid + '\n층 =' + floor+'\n전화번호 ='+tel)
                elif terminalid == None:
                    print('\n시설별 시퀀스 번호=' + sn + '\n취급 품목 =' + facilityItem + '\n시설명/매장명 =' + facilityName + '\n시설 위치 =' + location +'\n취급 품목 브랜드 ='+goods+ '\n서비스 시간 =' + servicetime + \
                         '\n층 =' + floor + '\n전화번호 =' + tel)
                elif tel !=None and goods !=None:
                    print(
                        '\n시설별 시퀀스 번호=' + sn + '\n취급 품목 =' + facilityItem + '\n시설명/매장명 =' + facilityName + '\n시설 위치 =' + location + '\n취급 품목 브랜드 ='+goods+'\n서비스 시간 =' + servicetime + \
                        '\n터미널 =' + terminalid + '\n층 =' + floor + '\n전화번호 =' + tel)
        if count == 0:
            print('\n해당 품목이 면세점에 없습니다.')

        print("=========공항 지도를 웹으로 연결하시겠습니까?===========")
        print("\n=========예(y)/아니오(n)==========================\n")
        yn = input()

        if yn == 'y' or yn == 'Y':
            print('\n공항 지도 보기를 선택하였습니다.')
            map()
        else:
            print('\n공항 지도 연결을 건너뛰었습니다.')



def searchNodutyFacilities():
    from urllib import parse
    print('===========비면세구역 매장 검색===========')

    print("\n\n")

    key = 'QydOrzDVYNDcxRwTCTjElQ8FWVC7fQgJ8JVlglIlMmFtva3gU65%2BRmV%2FlyxorjQzmRAiXGxM%2F2E1PXAC56NWdg%3D%3D'

    dic = {'0': '공항시설', '1': '공항명소', '2': '일반쇼핑', '3': '음식점'}
    print('     0:공항 시설         1:공항 명소      2:일반 쇼핑       3:음식점      ')

    url = 'http://openapi.airport.kr/openapi/service/FacilitiesInformation/getFacilitesInfo?serviceKey='+key+'&pageNo=1&startPage=1&numOfRows=320&pageSize=320&lang=K&lcduty=N'

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

    store = input('원하는 편의시설의 번호를 입력하세요:\n')

    for child in root.iter('item'):
        if dic[store] in child.find('lcategorynm').text:
            print(child.find('facilitynm').text)

    store = input('상세하게 알고 싶은 매장을 입력하세요:')

    for child in root.iter('item'):
        if store in child.find('facilitynm').text:
            name = child.find('facilitynm').text
            floor = child.find('floorinfo').text
            location = child.find('lcnm').text
            servicetime=child.find('servicetime').text
            serialnum= child.find('sn').text
            if child.find('tel')!=None:
                tel = child.find('tel').text
            else:
                tel = None
            terminalId = child.find('terminalid').text

            if tel != None:
                print('\n가게 이름 ='+name+'\n층 ='+floor+'\n매장 위치 ='+location+'\n영업 시간 ='+servicetime+'\n매장 번호 ='+\
                  serialnum+'\n전화 번호 ='+tel+'\n터미널 ='+terminalId)
            elif tel == None:
                print( '\n가게 이름 =' + name + '\n층 =' + floor + '\n매장 위치 =' + location + '\n영업 시간 =' + servicetime + '\n매장 번호 =' + \
                    serialnum + '\n터미널 =' + terminalId)

    print("=========공항 지도를 웹으로 연결하시겠습니까?===========")
    print("\n=========예(y)/아니오(n)==========================\n")
    yn = input()

    if yn =='y' or yn == 'Y':
        print('\n공항 지도 보기를 선택하였습니다.')
        map()
    else:
        print('\n공항 지도 연결을 건너뛰었습니다.')

def map():
    new_url = 'https://www.airport.kr/ap/ko/map/mapInfo.do'
    return webbrowser.open_new(new_url)
