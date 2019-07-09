import requests
import json
import time


def a():

    loginurl = 'https://sx.byebyetext.com/api/app/users/third/login'
    headers1 = {
        "User-Agent": "okhttp/3.11.0",
        'accept-encoding': 'gzip',
        'content-length': '370',
        'Host': 'sx.byebyetext.com',
        'content-type': 'application/x-www-form-urlencoded'
    }
    data= 'openId=oR6sd1dTvATHpczuv2mpBicdnIOU&unionId=oGEegwG5z30-BQJQBXcSM-coEcNA&nickName=wxid_qfpud60bmqj421&avatarUrl=http%3A%2F%2Fthirdwx.qlogo.cn%2Fmmopen%2Fvi_32%2FQ0j4TwGTfTLn2wBLGGSDR4Efhpb48XeTFUKCqicUddGGbUKBRdBZBOt7r8dcrXgSaNfdgxTuB1Le2J28XjZZZFQ%2F132&userGender=2&authType=1&countryCode=CN&appVersion=3.5.0&deviceInfo=unknown%2Funknown%2F8.1.0&platformId=1&deviceId='
    rsp2 = requests.post(loginurl, headers=headers1, data=data)
    json1 = json.loads(rsp2.content)
    data_token = json1['data']
    token = data_token['token']
    b(token)


def b(token):

    url = "https://sx.byebyetext.com/api/app/users/6301/voices?"
    kw = {
        "lastId": "null",
        'moduleId': '2'
    }
    headers2 = {
        "User-Agent": "okhttp/3.11.0",
        'accept-encoding': 'gzip',
        'authorization': 'Bearer '+token,
        'Host': 'sx.byebyetext.com',
        'content-type': 'application/x-www-form-urlencoded'
    }
    rsp = requests.get(url, params=kw, headers=headers2)
    a = rsp.content.decode("raw_unicode_escape")
    b = json.loads(a)
    c = b['data']
    # print(c)
    for d in c:
        e = time.localtime(int(d['created_at']))
        f = time.strftime("%Y-%m-%d %H:%M:%S", e)

        print(d['voice_url'],f,d['voice_len']+'秒',d['topic_name'])

if __name__ == '__main__':
    a()

