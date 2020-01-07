import smtplib
from email.mime.text import MIMEText
class SendEmail:
    global send_user
    global email_host
    global password
    email_host = "smtp.qq.com"
    send_user = "3538615590@qq.com"
    password = "lppknvhochfidcbe"
    EMAIL_HOST_PASSWORD = 'lppknvhochfidcbe'

    def send_email(self, user_list, sub, content):
        user = "ZX"+"<" + send_user + ">"
        message = MIMEText(content, _subtype='plain', _charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()


if __name__ == '__main__':
    send = SendEmail()
    user_list = ['1018404132@qq.com']
    sub = '接口测试结果'
    content = "我是一条咸鱼，啊哈哈哈哈哈哈"
    send.send_email(user_list, sub, content)