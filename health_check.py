#!/usr/bin/env python3

import shutil
import psutil
import socket
import os
import emails
import time


def cpu_usage_checker():
    usage = psutil.cpu_percent(1)
    return usage < 80


def disk_usage_checker(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


def memory_usage_checker():
    usage = psutil.virtual_memory()
    available = usage.available >> 20
    return available > 500


def check_localhost():
    localhost = socket.gethostbyname('localhost')
    if localhost == '127.0.0.1':
        return True


while True:
    subject = ''
    if not cpu_usage_checker():
        subject += 'Error - CPU usage is over 80%\n'
    if not disk_usage_checker('/'):
        subject += 'Error - Available disk space is less than 20%'
    if not memory_usage_checker():
        subject += 'Error - Available memory is less than 500MB'
    if not check_localhost():
        subject += 'Error - localhost cannot be resolved to 127.0.0.1'

    if not cpu_usage_checker() or not disk_usage_checker('/') or not memory_usage_checker() or not check_localhost():
        sender = 'automation@example.com'
        receiver = "{}@example.com".format(os.environ.get('USER'))
        body = 'Please check your system and resolve the issue as soon as possible.'
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send_email(message)

    time.sleep(60)
