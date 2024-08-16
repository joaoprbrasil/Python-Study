from datetime import datetime, timedelta, timezone

data_tokyo = datetime.now(timezone(timedelta(hours=+9)))

print(data_tokyo)
