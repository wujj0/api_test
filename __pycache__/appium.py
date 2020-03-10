#安装客户端包pip install Appium-Python-Client
#安装appium server : npm install -g appium(依赖android sdk)
#安装andriod sdk  
#android studio包含了Android sdk的安装工具

#adb devices -l目前连接到电脑上的设备

#准备工作  被测的应用，运行appium  server，启动被测的app运行的环境
#django
#paramiko 远程登录库

#1、登录服务器  2、检查是否有以前的版本再运行 3、如果有原来的代码包删除掉
#4、上传安装包文件（一般是winscp） 5、备份原来的产品安装目录 6、解压安装包文件
#7、运行run.sh，启动服务  8、浏览器登录页面验证服务是否启动


#自动安装测试环境

import paramiko
#创建sshclient示例对象
ssh = paramiko.SSHClient()
#调用方法，表示没有存储远程机器的公钥，允许访问
ssh,set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.1.104",22,"stt5","stt5200")
 
stdin,stdout,stderr = ssh.exec_command('ps -ef|grep apiteach')

output = stdout.read().decode()
print(output)

if 'python3 project/cherrypy_startup.py apiteach' in output:
    print("老版本程序运行中。。。准备结束")

    parts = output.split('')
    parts = [part for part in parts if part] #存成列表，最后一个判断part是否为空格

    pid=parts[1]

    ssh .exec_command(f"kill -9 {pid}") #或  ssh .exec_command("kill -9 " +pid)

ssh.exec_command("rm -f restapi_teach.zip")

sftp = ssh.open_sftp() #返回上传的对象，也可以用此修改配置文件
sftp.put(r"f:\tmp\a.zip",'/home/stt5/restapi-teach.zip')
sftp.close() 

