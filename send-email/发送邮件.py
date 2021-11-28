#! /usr/bin/env python
#coding=utf-8
from email.mime.text import  MIMEText# 发送一封邮件的内容
from email.mime.multipart import MIMEMultipart # 发送一封邮件的主题， 发送人和接收人
from email.mime.image import MIMEImage# 发送消息的图片
from email.mime.application import MIMEApplication# 发送邮件中的附件
from email.header import Header
import smtplib# python中定义的smtp程序, 用来发送邮件
# 写邮件，创建邮件
sender='18898186026@163.com'

# to_list=['18898186026@163.com',]
# sender='1192867487@qq.com'

to_list=['1192867487@qq.com',]

# cc_list=['18898186026@163.com']#抄送的邮箱
# bcc_list#表示密送
subject='python 发送邮件测试,设置发送的标题' #邮件的主题


#授权码
auth_code="填写自己的邮箱"
em=MIMEMultipart()# 创建一个邮件的对象，message.message
# 将信息传入对象中
em['Subject']=subject
em['From']=sender
em['To']=','.join(to_list)
# em['Cc']=','.join(cc_list)



#设置服务器的授权码,当做发送的密码
#设置发送的信息,设置为html 信息
content=MIMEText(open('index.htm','r',encoding='utf-8').read(),_subtype='html')
# 在html中有图片需要制定图片的地址
em.attach(content)
img=MIMEImage(open('test.png','rb').read())
# 发送到邮件服务器需要加上头信息说明img 的位置
img.add_header('Content-ID','<test>')# 设置绑定的样式 Content-ID <test>设置绑定的id
em.attach(img)

# 发送附件1

app=MIMEApplication(open('test.png','rb').read())
app.add_header('content-disposition', 'attachment', filename='test.png')
em.attach(app) #放置到发送的邮件中


#发送附件2
app=MIMEApplication(open('listname.txt','rb').read())
app.add_header('content-disposition','attachment',filename='test.txt')
em.attach(app)
# 如何来发送邮件
smtp = smtplib.SMTP()# 类不接受参数可以不用写()
smtp.connect('smtp.163.com')
smtp.login(sender,auth_code)# 连接数据库

smtp.send_message(em)# 接受的是email.message
# smtp.sendmail()# 接受的str 类型
smtp.close()# 关闭smtp 连接






