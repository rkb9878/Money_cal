import os
import time
from decouple import config

os.system('sudo kill -9 $(sudo lsof -t -i:8003)')

time.sleep(3)


os.system(
        'DJANGO_SETTINGS_MODULE=moneyCalc.settings /root/moneyCalc/env/bin/gunicorn moneyCalc.wsgi:application '
        ' --bind 0.0.0.0:8003 --chdir /root/moneyCalc --daemon --timeout 360 --workers=4')
