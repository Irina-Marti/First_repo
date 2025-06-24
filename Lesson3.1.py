from datetime import datetime


def get_days_from_today(date):
    requested_date = datetime.strptime(date, "%Y-%m-%d").date()
    date_today = datetime.today().date()
    diff_days = (date_today - requested_date).days

    return diff_days

input_date = "2020-10-09"
day_difference = get_days_from_today(input_date)

print("Today:", datetime.today().date())
print(f"Day diffence: {day_difference}")

