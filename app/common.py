from flask import current_app
from dateutil import tz


def local_timezone(date_time):
    timezone = current_app.config.get('TIMEZONE', 'Asia/Kolkata')
    from_tz = tz.gettz('UTC')
    to_tz = tz.gettz(timezone)
    utc = date_time.replace(tzinfo=from_tz)
    return utc.astimezone(to_tz)


def dt_format(dt):
    try:
        return dt.strftime(current_app.config.get('DATETIME_FORMAT', '%d-%m-%Y %H:%M:%S'))
    except:
        return None

