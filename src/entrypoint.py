# importing datetime, timedelta from datetime module
from datetime import datetime, timedelta
import argparse
import logging
import os

log = logging.getLogger(__name__)

class Default:
    """Shared default values for consistency."""

    DAYS = '7'

# list of days in a week
weekdaysList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']


# Get previous week from last_start date
def getPreviousByDay(inputDay, start_date=None, daysAgo=7):
    # check whether the start date is None
    if start_date is None:
        # assiging today's date(current date) to the start date
        start_date = datetime.today().replace(microsecond=0)
        # getting the weekday number
        dayNumber = start_date.weekday()
        # Get the index of the target weekday
        dayNumberTarget = weekdaysList.index(inputDay)
        # getting the last weekday
        daysAgo = (7 + dayNumber - dayNumberTarget) % 7
    # Subtract the above number of days from the current date(start date)
    # to get the last week's date of the given day
    targetDate = start_date - timedelta(days=daysAgo)
    # returning the last week's date of the input date
    return targetDate.date()


def parse_args():
    parser = argparse.ArgumentParser(description="Greetings")
    parser.add_argument("--date", required=True)
    parser.add_argument("--days", required=False, default=Default.DAYS)
    return parser.parse_args()


def main():
    date_format = '%Y-%m-%d'
    args = parse_args()
    date = args.date
    days = args.days
    last_start_dt = datetime.strptime(date, date_format)
    targetDate = getPreviousByDay(last_start_dt.strftime('%A'), last_start_dt, int(days))

    with open(os.environ['GITHUB_OUTPUT'], 'at') as f:
        f.write(f"start_date={str(targetDate)}\n")
        f.write(f"end_date={date}\n")


if __name__ == "__main__":
    main()
