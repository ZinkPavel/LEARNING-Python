import datetime


def increment_days_to_date(year, month, day, extra_days):
    return datetime.date(year, month, day) + datetime.timedelta(days=extra_days)


if __name__ == "__main__":
    date = input().split(" ")
    date = map(int, date)
    extra_days = int(input())
    date = increment_days_to_date(*date, extra_days)
    print(f"{date.year} {date.month} {date.day}")
