from datetime import datetime

now = datetime.now()
date= ('%02d/%02d/%04d' % (now.month, now.day, now.year))
time= ('%02d:%02d:%02d' % (now.hour, now.minute, now.second))
print(f"({date}) ({time})")