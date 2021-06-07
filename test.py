from datetime import datetime
time = datetime.now()
print('{},{}'.format(time.strftime('%m/%d/%y'),time.strftime('%H:%M')))