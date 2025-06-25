from datetime import datetime


def get_days_from_today(date):
    try:
        requested_date = datetime.strptime(date, "%Y-%m-%d").date()
        date_today = datetime.today().date()
        diff_days = (date_today - requested_date).days
        return diff_days

    except ValueError:
        return "Date input in the wrong format. Please enter the date in this format: YYYY-MM-DD"



input_date = "2020-10-06"
day_difference = get_days_from_today(input_date)

print("Today:", datetime.today().date())
print(f"Day diffence: {day_difference}")

