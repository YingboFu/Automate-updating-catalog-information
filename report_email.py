#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails

descriptions_directory = 'supplier-data/descriptions'
body = ""
keys = ['name', 'weight']

for filename in os.listdir(descriptions_directory):
    if filename.endswith('.txt'):
        count = 0
        with open(os.path.join(descriptions_directory, filename), encoding='utf-8') as file:
            for line in file:
                if count == 2:
                    break
                body += "{}: {}".format(keys[count], line.strip()) + '<br/>'
                count += 1
        body += '<br/>'

title = 'Processed Update on ' + date.today().strftime("%B %d, %Y")


if __name__ == "__main__":
    reports.generate_report('/tmp/processed.pdf', title, body)

    sender = 'automation@example.com'
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    message = emails.generate_email(sender, receiver, subject, body, '/tmp/processed.pdf')
    emails.send_email(message)

