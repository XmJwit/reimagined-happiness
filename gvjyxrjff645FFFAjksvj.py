# -*- coding: UTF-8 -*-
import requests as req
import json
import sys
import time
import random
# 先注册azure应用,确保应用有以下权限:
# files:	Files.Read.All、Files.ReadWrite.All、Sites.Read.All、Sites.ReadWrite.All
# user:	User.Read.All、User.ReadWrite.All、Directory.Read.All、Directory.ReadWrite.All
# mail:  Mail.Read、Mail.ReadWrite、MailboxSettings.Read、MailboxSettings.ReadWrite
# 注册后一定要再点代表xxx授予管理员同意,否则outlook api无法调用


path = sys.path[0]+r'/chbiiuc384ySB938bccb_sbd8JCBYWos3.txt'
num1 = 0






def gettoken(refresh_token):
    headers = {'Content-Type': 'application/x-www-form-urlencoded',
               }
    data = {'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': id,
            'client_secret': secret,
            'redirect_uri': 'http://localhost:53689/'
            }
    html = req.post(
        'https://login.microsoftonline.com/common/oauth2/v2.0/token', data=data, headers=headers)
    jsontxt = json.loads(html.text)
    refresh_token = jsontxt['refresh_token']
    access_token = jsontxt['access_token']
    return access_token


def main():
    fo = open(path, "r+")
    refresh_token = fo.read()
    fo.close()
    global num1
    localtime = time.asctime(time.localtime(time.time()))
    access_token = gettoken(refresh_token)
    headers = {
        'Authorization': access_token,
        'Content-Type': 'application/json',
    }
    print('此次运行开始时间为 :', localtime)
    try:
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive/root', headers=headers).status_code == 200:
            num1 += 1
            print("1调用成功"+str(num1)+'次')
            time.sleep(random.randint(2, 5))
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive', headers=headers).status_code == 200:
            num1 += 1
            print("2调用成功"+str(num1)+'次')
            time.sleep(random.randint(2, 5))
        if req.get(r'https://graph.microsoft.com/v1.0/drive/root', headers=headers).status_code == 200:
            num1 += 1
            print('3调用成功'+str(num1)+'次')
            time.sleep(random.randint(2, 5))
        if req.get(r'https://graph.microsoft.com/v1.0/users ', headers=headers).status_code == 200:
            num1 += 1
            print('4调用成功'+str(num1)+'次')
            time.sleep(random.randint(2, 5))
        if req.get(r'https://graph.microsoft.com/v1.0/me/messages', headers=headers).status_code == 200:
            num1 += 1
            print('5调用成功'+str(num1)+'次')
            time.sleep(random.randint(2, 5))
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules', headers=headers).status_code == 200:
            num1 += 1
            print('6调用成功'+str(num1)+'次')
            time.sleep(random.randint(2, 5))
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders/inbox/messageRules', headers=headers).status_code == 200:
            num1 += 1
            print('7调用成功'+str(num1)+'次')
            time.sleep(random.randint(2, 5))
        if req.get(r'https://graph.microsoft.com/v1.0/me/drive/root/children', headers=headers).status_code == 200:
            num1 += 1
            print('8调用成功'+str(num1)+'次')
            time.sleep(random.randint(2, 5))
        if req.get(r'https://api.powerbi.com/v1.0/myorg/apps', headers=headers).status_code == 200:
            num1 += 1
            print('8调用成功'+str(num1)+'次')
            time.sleep(random.randint(2, 5))
        if req.get(r'https://graph.microsoft.com/v1.0/me/mailFolders', headers=headers).status_code == 200:
            num1 += 1
            print('9调用成功'+str(num1)+'次')
            time.sleep(random.randint(2, 5))
        if req.get(r'https://graph.microsoft.com/v1.0/me/outlook/masterCategories', headers=headers).status_code == 200:
            num1 += 1
            print('10调用成功'+str(num1)+'次')
            time.sleep(random.randint(2, 5))
    except:
        print("pass")
        pass

if __name__ == '__main__':
    cycle_count = random.randint(10, 20)
    for i in range(cycle_count):
        print("第"+str(i)+"次循环")
        time.sleep(random.randint(1200, 2400))
        main()
