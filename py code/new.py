import time
import pygame
from datetime import timedelta, datetime
import subprocess
def display_remaining_time(remaining_time):
remaining_days = remaining_time.days
remaining_seconds = remaining_time.seconds
remaining_minutes, remaining_seconds = divmod(remaining_seconds, 60)
remaining_hours, remaining_minutes = divmod(remaining_minutes, 60)
if remaining_days:
if remaining_days > 1:
remaining_days = '{:2d} days'.format(remaining_days)
else:
remaining_days = '{:2d} day'.format(remaining_days)
else:
remaining_days = ''
if remaining_hours:
if remaining_hours > 1:
remaining_hours = ' {:2d} hours'.format(remaining_hours)
else:
remaining_hours = ' {:2d} hour'.format(remaining_hours)
else:
remaining_hours = ''
if remaining_minutes:
if remaining_minutes > 1:
remaining_minutes = ' {:2d} minutes'.format(remaining_minutes)
else:
remaining_minutes = ' {:2d} minute'.format(remaining_minutes)
else:
remaining_minutes = ''
if remaining_seconds:
if remaining_seconds > 1:
remaining_seconds = ' {:2d} seconds'.format(remaining_seconds)
else:
remaining_seconds = ' {:2d} second'.format(remaining_seconds)
else:
remaining_seconds = ''
print('\rTime Remaining: {}{}{}{}'.format(remaining_days,
remaining_hours,
remaining_minutes,
remaining_seconds), end='')
print()
print('\t===============[Timedown]=============')
print('\t\t\t~~~~~~~~')
print('Enter Ctrl+C for exit ☻\n')
try:
while True:
date_now = datetime.today()
date_now_timestamp = int(date_now.timestamp())
new_year_date = datetime(year=date_now.year, month=1, day=22, hour=0, minute=0, second=0)
new_year_timestamp = int (new_year_date.timestamp())
remaining_time_seconds = new_year_timestamp - date_now_timestamp
remaining_time = timedelta(seconds=remaining_time_seconds)
display_remaining_time(remaining_time)
if date_now_timestamp > new_year_timestamp:
print("\r🎆~~~Happy New Year~~~🎆", end="")
break
time.sleep(1)
except KeyboardInterrupt:
exit()
time.sleep(1)
pygame.mixer.init()
pygame.mixer.music.load("Fireworks.mp3")
time.sleep(1)
pygame.mixer.music.play()
subprocess.run(["python", "Fireworks.py"])