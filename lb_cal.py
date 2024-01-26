from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz


cal = Calendar()
eastern = pytz.timezone('US/Eastern')


holidays = {
    "2024-01-01": "New Year's Day",
    "2024-01-15": "Martin Luther King Jr. Day",
    "2024-02-19": "Presidents' Day",
    "2024-05-27": "Memorial Day",
    "2024-06-19": "Juneteenth",
    "2024-07-04": "Independence Day",
    "2024-09-02": "Labor Day",
    "2024-10-14": "Columbus Day",
    "2024-11-05": "Election Day",
    "2024-11-11": "Veterans Day",
    "2024-11-28": "Thanksgiving Day",
    "2024-11-29": "Native American Heritage Day",
    "2024-12-25": "Christmas Day"
}


def is_holiday(date):
    return date.strftime("%Y-%m-%d") in holidays


def in_office_day(month):
    return {
        1: 4,  
        2: 0,  
        3: 1,  
        4: 2,  
        5: 3,  
        6: 4,  
        7: 0,  
        8: 1,  
        9: 2,  
        10: 3, 
        11: 4, 
        12: 0, 
    }[month]


start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 12, 31)
current_date = start_date

while current_date <= end_date:
    if current_date.weekday() < 5:  
        if not is_holiday(current_date):
            summary = "In Office" if current_date.weekday() == in_office_day(current_date.month) else "Remote"
            event = Event()
            event.add('summary', summary)
            event_date = eastern.localize(current_date)
            event.add('dtstart', event_date)
            event.add('dtend', event_date + timedelta(days=1))  
            event.add('transp', 'TRANSPARENT')  
            cal.add_component(event)
    current_date += timedelta(days=1)


with open('lb_calendar.ics', 'wb') as f:
    f.write(cal.to_ical())
