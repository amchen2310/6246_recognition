import smtplib
from email.header import Header
from email.mime.text import MIMEText
import urllib3



def check_internet_conn():
    http = urllib3.PoolManager(timeout=3.0)
    r = http.request('GET', 'google.com', preload_content=False)
    code = r.status
    r.release_conn()
    if code == 200:
        return True
    else:
        return False

def send_notice(receiver, msg_content):


    user = 'mcam.robot@gmail.com'
    pwd = 'noticefrommcam'
    msg = MIMEText(msg_content, 'plain', 'utf-8')
    msg['Subject'] = 'do not reply----only for auto notice'
    sender = 'mcam.robot@gmail.com'

    msg['From'] = sender
    msg['To'] = receiver
    mailhost = 'smtp.gmail.com'
    try:
        # check the receiver name

        # check the network connection
        check_internet_conn()

        smtpObj = smtplib.SMTP(mailhost, 587)
        # smtpObj.connect(mailhost,587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(user, pwd)
        smtpObj.sendmail(sender, receiver, msg.as_string())
        smtpObj.quit()
        print('INFO! email send success')
    except smtplib.SMTPException as e:
        print('ERROR! emial send error', e)