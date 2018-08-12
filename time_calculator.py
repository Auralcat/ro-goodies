"""Calculates the time between now and another time specified by the user
with the server's timezone as default"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import datetime

if __name__ == '__main__':
    current_time = datetime.now()
    print("Right now is %s" % current_time)
