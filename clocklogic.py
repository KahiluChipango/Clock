import calendar
from datetime import datetime, timedelta

class ClockLogic:
    def __init__(self):
        self.adjusted_time = datetime.now()

    def get_seconds(self):
        return self.adjusted_time.second

    def get_minutes(self):
        return self.adjusted_time.minute

    def get_hours(self):
        return self.adjusted_time.hour

    def get_day(self):
        return self.adjusted_time.day

    def get_week(self):
        return int(self.adjusted_time.strftime("%U"))  # Week number

    def get_month(self):
        return self.adjusted_time.month

    def get_year(self):
        return self.adjusted_time.year

    def adjust(self, years=0, months=0, days=0, hours=0, minutes=0, seconds=0):
        dt = self.adjusted_time
        year = dt.year + years
        month = dt.month + months
        while month > 12:
            month -= 12
            year += 1
        while month < 1:
            month += 12
            year -= 1
        day = min(dt.day, calendar.monthrange(year, month)[1])
        try:
            dt = dt.replace(year=year, month=month, day=day)
        except ValueError:
            dt = dt.replace(year=year, month=month, day=28)
        dt += timedelta(days=days, hours=hours, minutes=minutes, seconds=seconds)
        self.adjusted_time = dt

    def reset_time(self):
        self.adjusted_time = datetime.now()

    def tick(self):
        self.adjusted_time += timedelta(seconds=1)

    def get_time_str(self):
        return self.adjusted_time.strftime("%H:%M:%S")

    def get_date_str(self):
        return self.adjusted_time.strftime("Week %U | %A, %d %B %Y")
