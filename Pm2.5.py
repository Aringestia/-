def sendmail(message):
    import smtplib 
    from email.mime.text import MIMEText 


    from_addr = "programtester810048@gmail.com"
    to_addr = "810048@stu.nknush.kh.edu.tw"


    smtpssl=smtplib.SMTP_SSL("smtp.gmail.com", 465) 
    smtpssl.login(from_addr, "32279733qaz")

    msg = message
    mime=MIMEText(msg, "plain", "utf-8") 
    mime["Subject"] = "空氣品質監測"
    
    mime["From"] = "PM2.5監視器"
    mime["To"] = to_addr

    smtpssl.sendmail(from_addr, to_addr, mime.as_string())
    smtpssl.quit()

import requests, json
import urllib3
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


response = requests.get('https://opendata.epa.gov.tw/ws/Data/ATM00625/?$format=json', verify=False)

sites = response.json()

while True:
    for site in sites:
        if site['Site'] == '復興':
            sendmail("現在復興站測得空氣品質(pm2.5):"+site['PM25'])
            break
    time.sleep(60*60)
