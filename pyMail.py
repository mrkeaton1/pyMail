"""
Created on Thu Jul 16 08:23:52 2020

@author: Matthew Keaton
https://realpython.com/python-send-email/
"""

import smtplib, ssl, sys

port = 465  # For SSL
sender_email = "my_email"
receiver_email = "send_email"
task_name = sys.argv[1]

message = """\
Subject: Server Task {}

Hello Matthew,

Your task "{}" on the server has completed.

--This is an Automated Message--
""".format(task_name, task_name)

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, "password")
    server.sendmail(sender_email, receiver_email, message)
