from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib
import sys

cur_time = ""

def double_MD5(value):
    value = hashlib.md5(str(value).encode()).hexdigest()
    value = hashlib.md5(str(value).encode()).hexdigest()

    return get_code(value)

def get_code(value):
    letters = "".join([letter for letter in value if letter.isalpha()][:2])
    num = "".join([num for num in value[::-1] if num.isdigit()][:2])

    #for challenge uncomment 
    return letters + num # + "".join(value[-1])

if not sys.stdin.isatty():
    epoch_time = sys.stdin.read().strip('"').split()
    year, month, day, hour, minute, second = map(int, epoch_time)
    epoch_time = datetime(year, month, day, hour, minute, second, tzinfo=ZoneInfo("America/Chicago"))

else:
    epoch_time = datetime(1999, 12, 31, 23, 59, 59, tzinfo=ZoneInfo("America/Chicago"))

if cur_time:
    cur_time = cur_time.strip('"').split()
    year, month, day, hour, minute, second = map(int, cur_time)
    cur_time = datetime(year, month, day, hour, minute, second, tzinfo=ZoneInfo("America/Chicago"))
else:
    cur_time = datetime.now(ZoneInfo("America/Chicago"))

elapsed = int((cur_time - epoch_time).total_seconds())

elapsed -= elapsed % 60

sys.stdout.write(double_MD5(elapsed) + "\n")
sys.stdout.flush()
