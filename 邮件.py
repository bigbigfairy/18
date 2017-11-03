import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['subject'] = 'test'
msg['from'] = 'bigbigfairy@163.com'
msg['to'] = '1437594580@qq.com'
content = "你好，这是一封自动发送的邮件。"
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp=smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com', '25')
smtp.login('bigbigfairy@163.com','q154928.')
smtp.sendmail('bigbigfairy@163.com', '1437594580@qq.com', str(msg))
smtp.quit()

