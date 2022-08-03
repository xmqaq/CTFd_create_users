## ctfd_create_users
CTFd批量添加用户

本脚本功能是为CTFD批量添加用户，并自动为每个用户生成md5密码。

一、使用方法

1.所需环境：python3

2.需要登录当前CTFD管理员账户，在添加用户处抓取对应cookie和CSRF-token
![image](https://user-images.githubusercontent.com/50257557/182524219-70e57081-1cf8-4022-8db7-0320fafb0056.png)

输入必要信息

![image](https://user-images.githubusercontent.com/50257557/182524234-35d06b86-8e92-4971-b3c5-ddd7c3929a4d.png)

使用burp抓取数据包

![image](https://user-images.githubusercontent.com/50257557/182524263-48c2a1c7-1ac4-4dc3-b42a-f3a513a01192.png)

修改脚本header的CSRF-Token和Cookie信息

![image](https://user-images.githubusercontent.com/50257557/182524291-a43a1878-eaaf-44f8-a07e-367524fe6137.png)

修改此处为你运行CTFD服务器的ip

![image](https://user-images.githubusercontent.com/50257557/182524316-3102e269-c530-42f2-97fe-783f893e109b.png)

3.在脚本同一目录下准备需要添加用户的user.txt文件

![image](https://user-images.githubusercontent.com/50257557/182524338-1261e301-3f83-408f-bb5e-e52eb21d2f96.png)

4.运行脚本即可自动添加用户

![image](https://user-images.githubusercontent.com/50257557/182524371-9a82768e-0f73-4d0b-96a3-ce3538325a06.png)

![image](https://user-images.githubusercontent.com/50257557/182524385-6306b7c0-67fb-4677-867a-1e8f6a04f13d.png)


并在当前目录生成passwd.txt,里面对应添加用户的密码

![image](https://user-images.githubusercontent.com/50257557/182524411-88c3a21f-b90b-41b8-9896-53697ab62a38.png)

重复添加会显示用户已存在

![image](https://user-images.githubusercontent.com/50257557/182524442-e93fd4a0-75b6-4255-8059-8ddbeadec2ac.png)

退出当前管理员账户，cookie和csrf-token会失效

![image](https://user-images.githubusercontent.com/50257557/182524459-81603e44-7aeb-473c-aaf4-dea0024fccbf.png)
