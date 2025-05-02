from datetime import datetime, timezone
import sys
import hashlib

####   ALLOW FOR USER SELECTED TIME   ####
cur_time = ""
##########################################


####   DAY LIGHT SAVING TIME TOGGLE   ####
"""
This may or may not be necessary I am not sure. If it isn't replace
'DAYLIGHT_SAVINGS'
in line 59 with 3600 and delete this section. 
"""
DST = True
DAYLIGHT_SAVINGS = 0
if DST:
    DAYLIGHT_SAVINGS = 3600
##########################################

def double_MD5(value):
    value = hashlib.md5(str(value).encode()).hexdigest()
    value = hashlib.md5(str(value).encode()).hexdigest()
    return value

def get_code(value):
    ## GET THE FIRST 2 LETTERS FROM LEFT TO RIGHT ##
    letters = "".join([letter for index, letter in enumerate(value) if letter.isalpha()][:2])

    ## GET THE FIRST 2 NUMBERS FROM RIGHT TO LEFT ##
    nums = "".join([num for index, num in enumerate(value[::-1]) if num.isdigit()][:2])

    return letters + nums

#### CHECK FOR USER INPUT ####
if not sys.stdin.isatty():
    epoch_time = sys.stdin.read().strip()
else:
    epoch_time = "1999 12 31 23 59 59"

#### CONVERT EPOCH TIME INTO DATETIME OBJECT ####
epoch_time = epoch_time.strip('"').split()
year, month, day, hour, minute, second = map(int, epoch_time)
epoch_time = datetime(year, month, day, hour, minute, second, tzinfo=timezone.utc)

#### CONVERT CUR TIME INTO DATETIME OBJECT ####
if cur_time:
    cur_time = cur_time.strip().split()
    year, month, day, hour, minute, second = map(int, cur_time)
    cur_time = datetime(year, month, day, hour, minute, second, tzinfo=timezone.utc)
else:
    cur_time = datetime.now(timezone.utc)

#### CALCULATE ELAPSED TIME IN SECONDS ####
elapsed = int((cur_time - epoch_time).total_seconds()) - DAYLIGHT_SAVINGS

#### USE THE NEAREST MINUTE ####
elapsed -= elapsed % 60

hash_value = double_MD5(elapsed)
code = get_code(hash_value)
sys.stdout.write(code)

