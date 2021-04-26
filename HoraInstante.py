from datetime import datetime
from pytz import timezone
import pytz

#print(pytz.all_timezones)
print(datetime.now(pytz.timezone('Europe/Oslo')))
print(datetime.now(pytz.timezone('Pacific/Guadalcanal')))