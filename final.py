def send_email_new(email):
 import smtplib
 content="Third time test testing \nDo you want to take your business to the next level? Look no further than our services! Our team of experts is here to help you enhance your business through the latest technology. We specialize in providing customized solutions tailored to your specific needs. Our cutting-edge technology and innovative strategies are designed to help you reach your goals quickly and efficiently. \nContact us today to find out how we can help you maximize your profits!\n\n\nPlease let us know if you are interested.\n\n\nThanks and Regards,\n\nTechnology Support Team\nGISFY Private Limited"
 mail=smtplib.SMTP('smtp.office365.com', 587)
 mail.ehlo()
 mail.starttls()
 sender='techsupport@gisfy.co.in'
 recipient=email
 mail.login('techsupport@gisfy.co.in','Gisfy@1&%')
 header='To:'+recipient+'\n'+'From:' \
 +sender+'\n'+'subject:Enhance your business with technology services\n'+'\n'
 content=header+content
 mail.sendmail(sender, recipient, content)
 mail.close()


arr = ['ram@gisfy.co.in','siddhartha@gisfy.co.in','fatima@gisfy.co.in','azghar@gisfy.co.in']


for each in arr:
 send_email_new(str(each))