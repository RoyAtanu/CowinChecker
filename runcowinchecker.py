import logging
import checkslots as c
from time import sleep
import pathlib as pl
from decouple import config
from datetime import datetime as dt
import sys

pl.Path('log').mkdir(parents=False, exist_ok=True)

log = logging.getLogger('cowin')
log.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s | %(message)s', datefmt='%d-%m-%Y %H:%M:%S')

logfilename = 'conwin.log'
if config('LOG_FILE_NAME') != "":
    logfilename = config('LOG_FILE_NAME')
fh = logging.FileHandler(filename='log/' + logfilename, mode='a')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)

stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(logging.DEBUG)
stdout_handler.setFormatter(formatter)

log.addHandler(fh)
log.addHandler(stdout_handler)

interval = int(config('INTERVAL_IN_SEC'))

print('Cowin Slot Checker started...')
while True:
    print(f'Checking fot slots at {dt.now()}')
    c.checkSlots(log)
    print(f'Going to sleep for {interval} seconds...')
    sleep(interval)
