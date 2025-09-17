from datetime import datetime
import pytz

moscow_tz = pytz.timezone("Europe/Moscow")


def moscow_now():
    return datetime.now(moscow_tz).replace(tzinfo=None)