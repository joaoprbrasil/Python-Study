import pytz
from datetime import datetime

data = datetime.now(pytz.timezone('Asia/Tokyo'))
print(data)