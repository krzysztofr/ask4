# -*- coding: utf-8 -*-

import settings

import smtplib
from email.mime.text import MIMEText

print "Connecting to %s..." % settings.smtp['host'],
s = smtplib.SMTP(settings.smtp['host'])
s.login(settings.smtp['user'], settings.smtp['pass'])
print "OK"

for to in settings.recipients:
    msg = MIMEText(settings.message)
    msg['Subject'] = settings.subject
    msg['From'] = settings.from_email
    msg['To'] = to
    try:
        msg['Bcc'] = settings.bcc
    except AttributeError:
        pass
    print "Sending message to %s..." % to,
    s.sendmail(settings.from_email, [to], msg.as_string())
    print "OK"

print "Disconnecting from %s..." % settings.smtp['host'],
s.quit()
print "OK"
