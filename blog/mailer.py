#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#fromaddr = "builder@apps.cluster-3f3d.3f3d.sandbox1543.opentlc.com"
fromaddr = "Builder <kotestowy@interia.pl>"
toaddr = "kotestowy@interia.pl"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "New Build"

#Next, we attach the body of the email to the MIME message:
body = "Python test mail from Openshift!"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

#we have to convert the object to a string, and then use the same prodecure as above to send using the SMTP server
#import smtplib
server = smtplib.SMTP('poczta.interia.pl', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(toaddr, "!@#QWE123")
server.sendmail(fromaddr, toaddr, text)