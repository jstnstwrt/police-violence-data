#!/usr/bin/python3
import sys
import logging

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/html/police-violence-data')
print(sys.executable)

from police_violence_data import app as application