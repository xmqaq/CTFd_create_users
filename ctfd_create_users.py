import requests
import re
from hashlib import md5

ses = requests.session()
nonce_re = re.compile(r'\'?csrf(Nonce|_nonce)\'? ?[:=] "(.*)"')
url = 'http://yourip:8000'
username = 'admin'
password = 'admin'


def Login(username, passwd):
    def _extract_token(text):
        try:
            ses.headers.pop('CSRF-Token')
        except:
            pass
        nonce = nonce_re.findall(text)[0][1]
        ses.headers.setdefault('CSRF-Token', nonce)
    _extract_token(ses.get(url + '/login').text)
    _extract_token(ses.post(url + '/login', data={
        'name': username,
        'password': passwd,
        'nonce': ses.headers.get('CSRF-Token'),
    }).text)


def Create_user(name, password):
    data = {
        "name": name,
        "email": name + "@qq.com",
        "password": password,
        "type": "user",
        "country": "CN",
        "verified": 'false',
        "hidden": 'false',
        "banned": 'false',
        "fields": []
    }
    r = ses.post(url + '/api/v1/users', json=data)
    try:
        res = r.json()
    except:
        print('登录信息失效')
        return
    if res['success']:
        if name is str:
            print("账户:" + name + " 创建成功")
        else:
            zname = r'{0}'.format(name)
            print("账户:" + zname + " 创建成功")
    else:
        if name is str:
            print("账户:" + name + " 已存在")
        else:
            zname = r'{0}'.format(name)
            print("账户:" + zname + ' 已存在')


def hq_passwd(a):
    password = []
    for i in range(10000, 10080):
        s = md5(str(i).encode("utf-8")).hexdigest()
        passwd = str.upper(s[0:6])
        password.append(passwd)
    mima = password[a]
    return mima


def Pl_users():
    f = open("user.txt", 'r', encoding='utf-8')
    sz = 0
    for line in f.readlines():
        line = line.strip()
        password = hq_passwd(a=sz)
        f = open(f'passwd.txt', 'a')
        f.write(password + '\n')
        f.close()
        Create_user(name=line, password=password)
        sz += 1


Login(username, password)
Pl_users()
