# -*- coding: utf-8 -*-
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendmail(a):

    text=str(a)

    gmail_user="ekdskrnl105@gmail.com"
    gmail_pw="tkaudwls12!"

    to_addr=input("이메일 주소 : ")

    msg=MIMEMultipart('alternative')
    msg['From'] = gmail_user
    msg['To'] = to_addr
    msg['Subject'] = '항공정보'     # 제목
    msg.attach(MIMEText(text, 'plain', 'utf-8')) # 내용 인코딩

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

sendmail('sss')
