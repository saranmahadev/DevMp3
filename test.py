#import smtplib as s
#conn=s.SMTP('smtp.gmail.com',587)
#conn.ehlo()
#conn.starttls()
#conn.login('techgangsta1618@gmail.com','saran007.')
#conn.sendmail('techgangsta1618@gmail.com','sarandevnet@gmail.com','Subject: Hi\n\n Hi Saran Mahadev \n\n From Saran')

import messanger

# Mobile number registered in way2sms website.
phone = '+919409567000'

# Password in way2sms website.
password = ''

# Receiver mobile number.
receiver = '+919360644776'

# Text message that you want to send
message = """Hey Donald Trump,
Can write a python program which can send free text messages
"""

messanger.send(phone, password, receiver, message)