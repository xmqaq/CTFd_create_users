## ctfd_create_users

本脚本功能是为CTFD批量添加用户，并自动为每个用户生成md5密码。

一、使用方法

1.所需环境：python3

2.需要登录当前CTFD管理员账户，在添加用户处抓取对应cookie和CSRF-token

![image-20220803105107625](../../../我的笔记/images/image-20220803105107625.png)

输入必要信息抓取数据包

![image-20220803105318259](../../../我的笔记/images/image-20220803105318259.png)

![image-20220803105451041](../../../我的笔记/images/image-20220803105451041.png)

修改脚本header的CSRF-Token和Cookie信息

![image-20220803105846872](../../../我的笔记/images/image-20220803105846872.png)

修改此处为你运行CTFD服务器的ip

![image-20220803110212799](../../../我的笔记/images/image-20220803110212799.png)

3.在脚本同一目录下准备需要添加用户的user.txt文件

<img src="../../../我的笔记/images/image-20220803110012194.png" alt="image-20220803110012194" style="zoom:67%;" />

4.运行脚本即可自动添加用户

![image-20220803110346813](../../../我的笔记/images/image-20220803110346813.png)

![image-20220803110407613](../../../我的笔记/images/image-20220803110407613.png)

并在当前目录生成passwd.txt,里面对应添加用户的密码

<img src="../../../我的笔记/images/image-20220803110519974.png" alt="image-20220803110519974" style="zoom:67%;" />

重复添加会显示用户已存在

![image-20220803110723820](../../../我的笔记/images/image-20220803110723820.png)

退出当前管理员账户，cookie和csrf-token会失效

![image-20220803110928434](../../../我的笔记/images/image-20220803110928434.png)