import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "techsupport@gisfy.co.in"
you = "ram@gisfy.co.in"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you


html = """\
<html>
  <head></head>
  <body>
  <img src="https://media.licdn.com/dms/image/C4E0BAQHXwvsnLAmO-Q/company-logo_200_200/0/1630570398385/gisfy_private_limited_logo?e=2147483647&v=beta&t=bJyNt3yLpYPZezoVUFuhIHqOC1EXqZM2BChb3hF4_U8" alt="Italian Trulli">
    <p>Hi! NEW<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""


part2 = MIMEText(html, 'html')


msg.attach(part2)
mail = smtplib.SMTP('smtp.office365.com', 587)

mail.ehlo()

mail.starttls()

mail.login('techsupport@gisfy.co.in', 'Gisfy@1&%')
mail.sendmail(me, you, msg.as_string())
mail.quit()