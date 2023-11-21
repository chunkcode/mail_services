import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

me = "techsupport@gisfy.co.in"
you = "rampriyadas@outlook.in"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Enhance your business with technology services"
msg['From'] = me
msg['To'] = you


html = """\
<html>
  <head></head>
  <body>
   <h3>Dear Sir/Madam,</h3><br>
    <h3>Greeting from GISFY</h3><br>
    <h3>Do you want to take your business to the next level? Look no further than our services! Our team of experts is here to help you enhance your business through the latest technology. We specialize in providing customized solutions tailored to your specific needs. Our cutting-edge technology and innovative strategies are designed to help you reach your goals quickly and efficiently.</h3> 
   <br> <h3>Contact us today to find out how we can help you maximize your profits!</h3>
    <br><br>
<h4 style="margin: 0; padding: 0;">Thanks and Regards,</h4>
<h4 style="margin: 0; padding: 0;">Tech Support Team</h4>
<h4 style="margin: 0; padding: 0;">GISFY Private Limited</h4>
<h4 style="margin: 0; padding: 0;">DSL Abacus IT Park, Ground Floor,</h4>
<h4 style="margin: 0; padding: 0;">Uppal, Hyderabad, Telangana - Pin code: 500076, India</h4>

<h4 style="margin: 0; padding: 0;">Email: <a href="mailto:techsupport@gisfy.co.in">techsupport@gisfy.co.in</a>  , Mobile: <a href="tel:+919971777963">+91 9971777963</a></h4>
<img style="width: 20%; padding-top: 1%;" src="data:image/png;base64,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" alt="Italian Trulli">
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