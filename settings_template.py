# -*- coding: utf-8 -*-

recipients = (
    'john@example.com',
    'mary@example.com'
)

bcc = 'steve@example.com'

message = """
This is the contents of test message
"""

from_email = "Joe Example <joe@example.com>"

subject = "Test subject"

smtp = {
    'host' : 'smtp.example.com',
    'user' : 'username',
    'pass' : 'password'
}