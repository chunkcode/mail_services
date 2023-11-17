import smtplib

smtp_server = "smtpout.asia.secureserver.net"
smtp_port = 465
Email = "techsupport@gisfy.co.in"
Pass = "Gisfy@1&%"

from email.message import EmailMessage

arr = ['ram@gisfy.co.in','fatima@gisfy.co.in']

for each in arr:
 message = EmailMessage()
 message["Subject"] = "Enhance your business with technology services"
 message["From"] = Email
 message.set_content("Do you want to Test")
 message["To"] = each
 message["Cc"] = Email
 with smtplib.SMTP_SSL(smtp_server, smtp_port) as smtp:
    smtp.login(Email, Pass)
    smtp.send_message(message)
    
