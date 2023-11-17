import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
arr = ['ram@gisfy.co.in','siddhartha@gisfy.co.in','fatima@gisfy.co.in','azghar@gisfy.co.in']
for each in arr:
 msg = MIMEMultipart()
 msg.set_unixfrom('author')
 msg['From'] = 'techsupport@gisfy.co.in'
 msg['To'] = str(each)
 msg['Subject'] = 'Enhance your business with technology services'
 message = 'Do you want to take your business to the next level? Look no further than our services! Our team of experts is here to help you enhance your business through the latest technology. We specialize in providing customized solutions tailored to your specific needs. Our cutting-edge technology and innovative strategies are designed to help you reach your goals quickly and efficiently. \nContact us today to find out how we can help you maximize your profits!\n\n\nPlease let us know if you are interested.\n\n\nThanks and Regards,\n\nTechnology Support Team\nGISFY Private Limited'
 msg.attach(MIMEText(message))
 mailserver = smtplib.SMTP_SSL('smtpout.secureserver.net', 465)
 mailserver.ehlo()
 mailserver.login('techsupport@gisfy.co.in', 'Gisfy@1&%')
 mailserver.sendmail('techsupport@gisfy.co.in',str(each),msg.as_string())
 mailserver.quit()