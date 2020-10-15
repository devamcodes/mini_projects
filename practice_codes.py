"""
Project: practicing the course code here for the first time.
Author:Devam A

Description:Datetime module,
"""
from datetime import datetime, timezone, timedelta
time = datetime.now(timezone.utc) + timedelta(hours= 5.50)
print(datetime.now())
print(time.strftime('%d-%m-%Y %H:%M'))