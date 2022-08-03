import json
import requests
from hashlib import md5


def Create_user(name,password):
    headers = {
        "Content-Type": "application/json",
        "Cookie":"session=6a2ee3f6-a7e1-4439-90c4-273ae6187b6d",
        "CSRF-Token":"817ba5b85cb21357550ee4e14e1715627cd7589addcb21fb5848d4b3b04a39c"
               }

    data = {"name":name,
            "email":name+"@qq.com",
            "password":password,
            "type":"user",
            "country": "CN",
            "verified":'false',
            "hidden":'false',
            "banned":'false',
            "fields":[]
            }
    r=requests.post('http://yourip:8000/api/v1/users',data=json.dumps(data),headers=headers)

    nr=str(r.text)

    cz=str('"success": false')

    if str('created') in nr:

        if name is str:

            print("账户:"+name+" 创建成功")

        else:

            zname=r'{0}'.format(name)

            print("账户:"+zname+" 创建成功")

    elif cz in nr:

        if name is str:

            print("账户:"+name+" 已存在")

        else:

            zname = r'{0}'.format(name)

            print("账户:"+zname+' 已存在')

    else:
        print('当前cookie和Csrf-Token已失效，请重新获取。')
        

def hq_passwd(a):

    password = []

    for i in range(10000, 10080):

        s = md5(str(i).encode("utf-8")).hexdigest()

        passwd = str.upper(s[0:6])

        password.append(passwd)

    mima=password[a]

    return mima

def Pl_users():

    f=open("user.txt",'r',encoding='utf-8')

    sz = 0

    for line in f.readlines():

        line=line.strip()

        password=hq_passwd(a=sz)

        f = open(f'passwd.txt', 'a')

        f.write(password+'\n')

        f.close()

        Create_user(name=line,password=password)

        sz+=1

Pl_users()




